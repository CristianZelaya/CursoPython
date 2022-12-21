from Computadora import Computadora
from Monitor import Monitor
from Orden import Orden
from Raton import Raton
from Teclado import Teclado

teclado = Teclado('BT', 'Lenovo')
teclado2 = Teclado('Inalambrico', 'Asus')
teclado3 = Teclado('BT', 'Logitech')

raton = Raton('USB', 'Lenovo')
raton2 = Raton('USB', 'Hp')
raton3 = Raton('Inalambrico', 'Microsoft')

monitor = Monitor('Lenovo', '24"')
monitor2 = Monitor('Sony', '32"')
monitor3 = Monitor('Xiaomi', '40"')

computadora = Computadora('Mi PC', monitor, teclado, raton)
computadora2 = Computadora('Mi PC 2', monitor2, teclado2, raton2)
computadora3 = Computadora('MiPC3', monitor3, teclado3, raton3)

print('Creando Orden'.center(50, '-'))

computadoras = [computadora, computadora2]
orden = Orden(computadoras)
orden.agregar_computadora(computadora3)
print(orden)