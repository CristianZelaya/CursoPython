import sys

from logger_base import log
from usuario import Usuario
from usuario_dao import UsuarioDao


def main():
    menu = '''
    --- Menú App Usuario ---
    1. Lista de Usuarios
    2. Insertar Usuario
    3. Actualizar Usuario
    4. Eliminar Usuario
    5. Salir
    '''
    try:
        opcion = None
        while opcion != 5:
            print(menu)
            opcion = int(input('Ingresa una opción (1 al 5): '))

            if opcion == 1:
                print('1. Lista de Usuarios')
                usuarios = UsuarioDao().seleccionar()
                for usuario in usuarios:
                    print(usuario)
            elif opcion == 2:
                print('2. Insertar Usuario')
                username = input('Ingresa el username del usuario: ')
                password = input('Ingresa el password del usuario: ')
                usuario = Usuario(username=username, password=password)
                usuario_insertado = UsuarioDao.insertar(usuario)
                log.info(usuario_insertado)
            elif opcion == 3:
                print('3. Actualizar Usuario')
                id_usuario = int(input('Ingresa el id de usuario: '))
                username = input('Ingresa el username para editar: ')
                password = input('Ingresa el password para editar: ')
                usuario = Usuario(id_usuario=id_usuario, username=username, password=password)
                usuario_actualizado = UsuarioDao.actualizar(usuario)
                log.info(usuario_actualizado)
            elif opcion == 4:
                print('4. Eliminar Usuario')
                id_usuario = int(input('Ingresa el id del usuario a eliminar: '))
                usuario = Usuario(id_usuario=id_usuario)
                usuario_eliminado = UsuarioDao.eliminar(usuario)
                log.info(usuario_eliminado)
            elif opcion == 5:
                print('5. Saliendo...')
            else:
                print(f'{opcion} no es una opcion del menu')
        else:
            log.info('Salimos de la aplicación')

    except Exception as e:
        log.error(f'Ocurrio un error: {e}')
        sys.exit()


main()
