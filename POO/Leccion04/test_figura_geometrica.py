from Cuadrado import Cuadrado

cuadrado = Cuadrado(5, 'rojo')
#print(cuadrado.alto)
#print(cuadrado.ancho)
#print(cuadrado.color)
print(f'Calculo del area: {cuadrado.calcular_area()}')

# MRO - Method Resolution Order
print(Cuadrado.mro())