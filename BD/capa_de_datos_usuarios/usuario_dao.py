import sys

from cursor_del_pool import CursorDelPool
from logger_base import log
from usuario import Usuario


class UsuarioDao:

    _SELECT = 'SELECT * FROM usuario where status=true'
    _INSERT = 'INSERT INTO usuario(username, password) VALUES (%s, %s)'
    _UPDATE = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _DELETE = 'UPDATE usuario SET status=False WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        try:
            with CursorDelPool() as cursor:
                cursor.execute(cls._SELECT)
                registros = cursor.fetchall()
                usuarios = []
                for registro in registros:
                    usuario = Usuario(registro[0], registro[1], registro[2])
                    usuarios.append(usuario)
                return usuarios
        except Exception as e:
            log.error(f'Ocurrio un error en el select: {e}')
            sys.exit()

    @classmethod
    def insertar(cls, usuario):
        try:
            with CursorDelPool() as cursor:
                valores = (usuario.username, usuario.password)
                cursor.execute(cls._INSERT, valores)
                log.debug(f'Usuario Insertado con exito: {usuario}')
                return cursor.rowcount
        except Exception as e:
            log.error(f'Ocurrio un error en el insert: {e}')
            sys.exit()

    @classmethod
    def actualizar(cls, usuario):
        try:
            with CursorDelPool() as cursor:
                valores = (usuario.username, usuario.password, usuario.id_usuario)
                cursor.execute(cls._UPDATE, valores)
                log.debug(f'Usuario actualizado con exito: {usuario}')
                return cursor.rowcount
        except Exception as e:
            log.error(f'Ocurrio un error en el update: {e}')
            sys.exit()

    @classmethod
    def eliminar(cls, usuario):
        try:
            with CursorDelPool() as cursor:
                valor = (usuario.id_usuario,)
                cursor.execute(cls._DELETE, valor)
                log.debug(f'Usuario eliminado con exito: {usuario}')
                return cursor.rowcount
        except Exception as e:
            log.error(f'Ocurrio un error en el delete: {e}')
            sys.exit()

if __name__ == '__main__':
    # Insertar
    #usuario = Usuario(username='fany', password='brabusd4314')
    #usuarios_insertados = UsuarioDao.insertar(usuario)
    #log.debug(f'Usuario insertado: {usuarios_insertados}')

    # Actualizar
    #usuario = Usuario(2, 'Fany', 'brabus.01')
    #usuarios_actualizados = UsuarioDao.actualizar(usuario)
    #log.debug(f'Usuario actualizado: {usuarios_actualizados}')

    usuario = Usuario(id_usuario=1)
    usuario_eliminado = UsuarioDao.eliminar(usuario)
    log.debug(f'Usuario eliminado: {usuario_eliminado}')

    # Seleccionar
    usuarios = UsuarioDao.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)
