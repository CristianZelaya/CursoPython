import psycopg2 as bd

conexion = bd.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)

try:
    # conexion.autocommit = False
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    valores = ('David', 'Zelaya', 'davidz@gmail.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET estado=false where id_persona = 1'
    cursor.execute(sentencia)
    conexion.commit()
    print('Termina la transaccion')
except Exception as e:
    conexion.rollback()
    print(f'Se hizo rollback de la transaccion: {e}')
finally:
    print(f'Se cerro la conexion')
    conexion.close()

# With automatizado toddo lo que tiene que ver con trasacciones, sin necesidad de hacerlo manualmente