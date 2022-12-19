from Cuadrado import Cuadrado
from FiguraGeometrica import FiguraGeometrica
from Rectangulo import Rectangulo

# No se puede instanciar una clase abstracta
# figura = FiguraGeometrica()

print('Creacion objeto cuadrado'.center(50, '-'))
cuadrado = Cuadrado(-5, 'rojo')
print(cuadrado)

# MRO - Method Resolution Order
#print(Cuadrado.mro())

print('Creacion objeto rectangulo'.center(50, '-'))
rectangulo = Rectangulo(3, 8, 'Azul')
print(rectangulo)
rectangulo.ancho = -5
print(rectangulo)
print(rectangulo.color)
