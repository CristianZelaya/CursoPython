from logger_base import log
from psycopg2 import pool
import sys
class Conexion:

    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = 'localhost'
    _conexion = None
    _cursor = None
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      database=cls._DATABASE
                                                      )
                log.debug(f'Creación del pool exitoso: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.debug(f'Ocurrio un error al obtener el pool: {e}')
                sys.exit()
        else:
            return  cls._pool

    @classmethod
    def obtenerConexion(cls):
        # objeto de conexion a la base de datos
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexión obtenida del pool: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos la conexion al pool: {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerConexion().closeall()

    @classmethod
    def obtenerCursor(cls):
        pass

if __name__ == '__main__':
    conexion = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion)
    conexion2 = Conexion.obtenerConexion()