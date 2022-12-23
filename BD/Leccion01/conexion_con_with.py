import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)

# fetchone
try:
    with conexion as conn:
        with conn.cursor() as curs:
            id_persona = input('Proporciona el valor de id persona: ')
            curs.execute(f'SELECT * FROM persona where id_persona = {id_persona}')
            print(curs.fetchone())
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    print(f'Se cerro la conexion')
    conexion.close()
