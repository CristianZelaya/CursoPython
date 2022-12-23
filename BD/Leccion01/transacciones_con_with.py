import psycopg2 as bd

conexion = bd.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            cursor = conexion.cursor()
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
            valores = ('Ana', 'Ventura', 'anav@gmail.com')
            cursor.execute(sentencia, valores)

            sentencia = 'UPDATE persona SET estado=false where id_persona = 6'
            cursor.execute(sentencia)
except Exception as e:
    print(f'Se hizo rollback de la transaccion: {e}')
finally:
    print(f'Se cerro la conexion')
    conexion.close()
print('Termina la transaccion, se hizo commit')

# With automatizado toddo lo que tiene que ver con trasacciones, sin necesidad de hacerlo manualmente