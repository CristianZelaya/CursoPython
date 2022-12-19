from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print('Creacion objeto cuadrado'.center(50, '-'))
cuadrado = Cuadrado(5, 'rojo')
print(cuadrado)

# MRO - Method Resolution Order
#print(Cuadrado.mro())

print('Creacion objeto rectangulo'.center(50, '-'))
rectangulo = Rectangulo(3, 8, 'Azul')
print(rectangulo)
rectangulo.color = 'Verde'
print(rectangulo)
print(rectangulo.color)
