from Orden import Orden
from Producto import Producto

producto = Producto('Camisa', 100)
producto2 = Producto('Pantalon', 150)

producto3 = Producto('Calcetines', 50)
producto4 = Producto('Falda', 70)

productos = [producto, producto2]
productos2 = [producto3, producto4]

orden = Orden(productos)
orden2 = Orden(productos2)


orden.agregar_producto(producto3)
orden.agregar_producto(producto4)
print(orden)
print(orden.calcular_total())

print(orden2)
print(orden2.calcular_total())