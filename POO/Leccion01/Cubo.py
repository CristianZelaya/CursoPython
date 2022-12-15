class Cubo:

    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundidad

def init():

    print('--- Calcular volumen de un cubo ---')

    ancho = float(input('Ingresa el ancho del cubo: '))
    alto = float(input('Ingresa el alto del cubo: '))
    profundidad = float(input('Ingresa la profundidad del cubo: '))

    cubo = Cubo(ancho, alto, profundidad)

    print(f'El volumen del cubo es: {cubo.calcular_volumen()}')

init()