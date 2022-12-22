archivo = None
archivo2 = None
try:
    archivo = open('prueba.txt', 'r', encoding='utf-8')
    #print(archivo.read())

    # Leer parte del archivo
    #print(archivo.read(5))
    #print(archivo.read(3))

    #Leer lineas completas
    #print(archivo.readline())
    #print(archivo.readline())

    # iterar cada linea
    #for linea in archivo:
    #    print(linea)

    # leer lineas
    #print(archivo.readlines())

    # acceder a una linea
    #print(archivo.readlines()[0])

    # abrir un nuevo archivo
    # a - anexar informacion
    archivo2 = open('copia.txt', 'w+', encoding='utf-8')
    archivo2.write(archivo.read())
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    if archivo != None:
        archivo.close()
        print('Se cerro el archivo 1')
    if archivo2 != None:
        archivo2.close()
        print('Se termino de copiar y se cerro el archivo')