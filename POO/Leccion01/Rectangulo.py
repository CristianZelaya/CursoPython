class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

def init():

    print('--- Calcular area de un rectangulo ---')
    base = float(input('Ingresa la base del rectangulo: '))
    altura = float(input('Ingresa la altura del rectangulo: '))

    rectangulo = Rectangulo(base, altura)

    print(f'El area del rectangulo es: {rectangulo.calcularArea()}')

init()