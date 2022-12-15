# Listas en python

"""nombres = ['Cristian', 'Stefhani', 'David', 'Josué']

for nombre in nombres:
    print(f'Nombre: {nombre}')
else:
    print('No existen más nombres en la lista')

print(f'Forma individual => {nombres[0]}')
print(f'Forma individual inversa => {nombres[-1]}')

# Mostrar rango de nombre Nota no incluye el nombre del ultimo valor solo muestra 0, 1
print(nombres[0:2])

# Desde el inicio hasta el indicado
print(nombres[:2])

# Desde el indicado hasta el final
print(nombres[1:])

# Cambiar un valor de la lista
nombres[0] = 'Arnulfo'
print(nombres)

# Preguntar el largo de una lista
print(len(nombres))

# Agregar un elemento a lista
nombres.append('Maryory')
print(nombres)

# Eliminar el ultimo elemento de la lista
nombres.pop()
print(nombres)

# Insertar un nombre en el indice especificado
nombres.insert(0, 'Cristian')
print(nombres)

# Elimina un nombre por su valor
nombres.remove('Arnulfo')
print(nombres)

# Eliminar el primer elemento de la lista
nombres.remove(nombres[0])
print(nombres)

# Eliminar un elemento por indice
del nombres[0]
print(nombres)

# Eliminar lista por completo
nombres.clear()
print(nombres)

# Eliminar lista por completo
del nombres
print(nombres)"""

"""# Ejercicio 1. Iterar un rango de 0 a 10 e imprimir números divisibles entre 3
print('Divisibles de 3')
for i in range(0, 10, 3):
    print(i)
else:
    print('Fin del ciclo')

# Ejercicio 2. Crear un rango de 2 a 6 e imprimirlos
print('Rango de 2 a 6')
for i in range(2, 7):
    print(i)
else:
    print('Fin del Ciclo')

# Ejercicio 3. Crear un rango de 3 a 10, pero con incremento de 2 en 2, en lugar de 1 en 1
print('Incremento de 2 en 2')
for i in range(3, 11, 2):
    print(i)
else:
    print('Fin del ciclo')"""

"""# Tuplas en Python es un tipo inmutable
frutas = ('Naranaja', 'Platano', 'Guayaba')
print(frutas)
print(len(frutas))
print(frutas[0])
print(frutas[-1])
print(frutas[0:2])
for fruta in frutas:
    print(fruta, end=' ')
# Cambiar el valor de una tupla
frutasLista = list(frutas)
frutasLista[0] = 'Pera'
frutas = tuple(frutasLista)
print('\n',frutas)
# Eliminar tupla
del frutas"""

"""tupla = (13, 1, 8, 3, 2, 5, 8)
lista = []
for i in tupla:
    if i < 5:
        lista.append(i)
print(lista)"""

"""# Coleccion set en python, no mantiene un orden y no almacena elementos repetidos
planetas = {'Marte', 'Jupiter', 'Venus'}
print(planetas)
print(len(planetas))
# reisar si esta presente un elemento
print('Marte' in planetas)
# Agregar mas elementos
planetas.add('Tierra')
print(planetas)
# Eliminar un elemento
planetas.remove('Tierra')
print(planetas)
# Elimina un elemento si se encuentra, no arroja un error
planetas.discard('Jupiters')
print(planetas)
# Limpiar un set
planetas.clear()
print(planetas)"""

# Diccionario en python
diccionario = {
    'nombre': 'Cristian',
    'apellido': 'Zelaya',
    'Edad': 28
}

print(len(diccionario))
print(diccionario['nombre'])
print(diccionario.get('apellido'))
diccionario['nombre'] = 'Arnulfo'
print(diccionario)

# Recorrer un diccionario
for llave, valor in diccionario.items():
    print(llave, valor)

for llave in diccionario.keys():
    print(llave)

for valor in diccionario.values():
    print(valor)

# comprobar si existe un elemento
print('nombre' in diccionario)
print('Arnulfo' in diccionario.values())

# Agregar un elemento
diccionario['cellphone'] = 75464859
print(diccionario)

# Remover un elemento
diccionario.pop('cellphone')
print(diccionario)

# limpiar diccionario
diccionario.clear()
print(diccionario)

# eliminar diccionario
del diccionario