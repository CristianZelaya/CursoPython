import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)

# Insertar varios registros
try:
    with conexion as conn:
        with conn.cursor() as curs:
            #nombre = input('Proporciona tu nombre: ')
            #apellido = input('Proporciona tu apellido: ')
            #email = input('Proporciona tu email: ')
            valores = (
                ('Pedro', 'Juarez', 'jp@hotmail.com'),
                ('Juan', 'Garcia', 'gj@gmail.com'),
                ('Sandra', 'Gomez', 'sg@gmail.com')
            )
            sentencia = f'INSERT INTO persona(nombre, apellido, email) values (%s, %s, %s)'
            curs.executemany(sentencia, valores)
            registros_insertados = curs.rowcount
            print(f'Registros insertados: {registros_insertados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    print(f'Se cerro la conexion')
    conexion.close()
