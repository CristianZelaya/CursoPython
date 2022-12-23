import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)

# crearemos un cursor
cursor = conexion.cursor()

#creamos la sentencia
sentencia = 'SELECT * FROM persona'

# ejecutamos la sentencia
cursor.execute(sentencia)

# almancenamos los registros, fetcall regresa todos los registros
registros = cursor.fetchall()

# imprimimos los registros
print(registros)

# cerramos la conexion
cursor.close()
conexion.close()