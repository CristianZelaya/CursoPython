import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)

try:
    with conexion as conn:
        with conn.cursor() as curs:
            sentencia = 'UPDATE persona SET status=false where id_persona=%s'
            valores = (
                (5,),
                (6,)
            )
            curs.executemany(sentencia, valores)
            registros_actualizados = curs.rowcount
            print(f'Registros eliminados: {registros_actualizados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    print(f'Se cerro la conexion')
    conexion.close()
