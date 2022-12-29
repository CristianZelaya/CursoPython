import sys

from psycopg2 import pool
from logger_base import log

class Conexion:

    _DATABASE='proyecto_db'
    _USERNAME='postgres'
    _PASSWORD='admin'
    _DB_PORT='5432'
    _HOST='localhost'
    _MIN_CON=1
    _MAX_CON=5
    _pool=None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      database=cls._DATABASE,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      host=cls._HOST)
                log.debug(f'Creación del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.debug(f'Ocurrio un error al obtener el pool: {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexión obtenida del pool con exito: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos la conexión al pool: {conexion}')

    @classmethod
    def cerrarConexion(cls):
        cls.obtenerConexion().closeall()

if __name__ == '__main__':
    conexion = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion)
    conexion2 = Conexion.obtenerConexion()

