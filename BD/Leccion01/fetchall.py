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
            #id_persona = input('Proporciona el valor de id persona: ')
            #llaves_primarias = (1, 2)
            entrada = input('Proporciona los ids a buscar (separador por comas): ')
            llaves_primarias = (tuple(entrada.split(',')),)
            print(llaves_primarias)
            curs.execute(f'SELECT * FROM persona WHERE id_persona IN {llaves_primarias}')
            registros = curs.fetchall()
            for registro in registros:
                print(registro)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    print(f'Se cerro la conexion')
    conexion.close()
