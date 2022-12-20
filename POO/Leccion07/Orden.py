from Producto import Producto


class Orden():

    numero_orden = 0

    def __init__(self, productos):
        Orden.numero_orden += 1
        self._id_oden = Orden.numero_orden
        self._productos = list(productos)

    # Agrega un producto nuevo a la orden
    def agregar_producto(self, producto):
        self._productos.append(producto)

    #Calcula el total de la orden
    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return f'Total orden: ${total}'

    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__() + ' | '
        return f'Orden: {self._id_oden} \nProductos: {productos_str}'

if __name__ == '__main__':
    producto = Producto('Camisa', 100)
    producto2 = Producto('Pantalon', 150)
    productos = [producto, producto2]
    orden = Orden(productos)
    print(orden)