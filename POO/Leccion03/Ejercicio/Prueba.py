from Vehiculo import *

print('Bienvenido, Ingresa un Vehiculo'.center(50, '-'))

color = input('Ingrese un color: ')
ruedas = int(input('Ingrese cantidad de ruedas: '))
vehiculo = Vehiculo(color, ruedas)
print(vehiculo)

print('Coche'.center(50, '-'))
color = input('Ingrese un color: ')
ruedas = int(input('Ingrese cantidad de ruedas: '))
velocidad = int(input('Ingrese la velocidad del coche: '))
coche = Coche(color, ruedas, velocidad)
print(coche)

print('Bicicleta'.center(50, '-'))
color = input('Ingrese un color: ')
ruedas = int(input('Ingrese cantidad de ruedas: '))
tipo = input('Ingrese el tipo de bicicleta: ')
bicicleta = Bicicleta(color, ruedas, tipo)
print(bicicleta)
