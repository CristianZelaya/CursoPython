# Bool contiene los valores true y false

# Tipos numericos, falso para 0 y true demas valores
print(f'Valor 0'.center(50, '-'))
valor = 0
resultado = bool(valor)
print(f'Valor de la variable es: {valor}, el resultado es: {resultado}')

print(f'Valor mayor a 0'.center(50, '-'))
valor = 1
resultado = bool(valor)
print(f'Valor de la variable es: {valor}, el resultado es: {resultado}')

print(f'Valores negativos'.center(50, '-'))
valor = -1
resultado = bool(valor)
print(f'Valor de la variable es: {valor}, el resultado es: {resultado}')

# Tipo str, false para '', true para los demas valores
print(f'Cadena vacia'.center(50, '-'))
valor = ''
resultado = bool(valor)
print(f'Valor de la variable es: {valor}, el resultado es: {resultado}')

print(f'Cadena con caracteres'.center(50, '-'))
valor = 'Hola'
resultado = bool(valor)
print(f'Valor de la variable es: {valor}, el resultado es: {resultado}')

# Tipo de colecciones, false para colecciones vacias, true para todas las demas colecciones
# Lista
print(f'Lista vacia'.center(50, '-'))
valor = []
resultado = bool(valor)
print(f'Valor de la variable es: {valor}, el resultado es: {resultado}')

print(f'Lista con valores'.center(50, '-'))
valor = [1, 2, 3]
resultado = bool(valor)
print(f'Valor de la variable es: {valor}, el resultado es: {resultado}')

# Diccionarios
print(f'Diccionario vacio'.center(50, '-'))
valor = {}
resultado = bool(valor)
print(f'Valor de la variable es: {valor}, el resultado es: {resultado}')

print(f'Diccionario con valores'.center(50, '-'))
valor = {
    'nombre': 'Cristian',
    'apellido': 'Zelaya',
    'edad': 28
}
resultado = bool(valor)
print(f'Valor de la variable es: {valor}, el resultado es: {resultado}')

# Tupla
print(f'Tupla vacia'.center(50, '-'))
valor = ()
resultado = bool(valor)
print(f'Valor de la variable es: {valor}, el resultado es: {resultado}')

print(f'Tupla con valores'.center(50, '-'))
valor = (1, 2, 3)
resultado = bool(valor)
print(f'Valor de la variable es: {valor}, el resultado es: {resultado}')

# Bool con sentencias de control
variable = ''
print(f'Sentencia de control if'.center(50, '-'))
print('Cadena vacia'.center(50, '-'))
if variable:
    print('Regreso verdadero')
else:
    print(f'Regreso falso: {variable}')

print(f'Cadena con valores'.center(50, '-'))
variable = 'Hola'
if variable:
    print(f'Regreso verdadero: {variable}')
else:
    print('Regresa falso')
