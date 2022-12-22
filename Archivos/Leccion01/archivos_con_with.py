# manejo de archivos de forma mas reducida utilizando with
#with open('prueba.txt', 'r', encoding='utf8') as archivo:
from ManejoArchivos import ManejoArchivos

with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())