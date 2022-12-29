import sys

from Cursor_del_pool import CursorDelPool
from logger_base import log

from Conexion import Conexion
from Persona import Persona


class PersonaDao:

    """
    DAO (DATA ACCESS OBJECT)
    CRUD (CREATE-READ-UPDATE-DELETE)
    """

    _SELECT = 'SELECT * from persona WHERE status=True ORDER BY id_persona'
    _INSERT = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    _UPDATE = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _DELETE = 'UPDATE persona SET status=False WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        try:
            with CursorDelPool() as cursor:
                cursor.execute(cls._SELECT)
                registros = cursor.fetchall()
                personas = []
                for registro in registros:
                    persona = Persona(registro[0], registro[1], registro[2], registro[3])
                    personas.append(persona)
                return personas
        except Exception as e:
            log.error(f'Ocurrio un error: {e}')
            sys.exit()

    @classmethod
    def insertar(cls, persona):
        try:
            with CursorDelPool() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERT, valores)
                log.debug(f'Persona insertada: {persona}')
                return cursor.rowcount
        except Exception as e:
            log.error(f'Ocurrio un error {e}')
            sys.exit()

    @classmethod
    def actualizar(cls, persona):
        try:
            with CursorDelPool() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                cursor.execute(cls._UPDATE, valores)
                log.debug(f'Persona actualizada: {persona}')
                return cursor.rowcount
        except Exception as e:
            log.error(f'Ocurrio un error {e}')
            sys.exit()

    @classmethod
    def eliminar(cls, persona):
        try:
            with CursorDelPool() as cursor:
                valor = (persona.id_persona,)
                cursor.execute(cls._DELETE, valor)
                log.debug(f'Persona eliminada: {persona}')
                return cursor.rowcount
        except Exception as e:
            log.error(f'Ocurrio un error: {e}')
            sys.exit()

if __name__ == '__main__':
    # Insertar un registro
    #persona1 = Persona(nombre='David', apellido='Zelaya', email='david@gmail.com')
    #persona_insertada = PersonaDao.insertar(persona1)
    #log.debug(f'Persona insertada: {persona_insertada}')

    # Actualizar un registro
    persona2 = Persona(4, 'Maryory', 'López', 'lopez@gmail.com')
    persona_actualizada = PersonaDao.actualizar(persona2)
    log.debug(f'Persona actualizada: {persona_actualizada}')

    # Eliminar un registro
    #persona3 = Persona(id_persona=17)
    #persona_eliminada = PersonaDao.eliminar(persona3)
    #log.debug(f'Persona eliminada: {persona_eliminada}')

    # Seleccionar objetos
    personas = PersonaDao.seleccionar()
    for persona in personas:
        log.debug(persona)
