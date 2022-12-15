class Aritmetica:
    """
    Clase aritmetica para realizar las acciones sumar, restar, etc
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sumar(self):
        return self.a + self.b

    def restar(self):
        return self.a - self.b

    def multiplicar(self):
        return self.a * self.b

    def dividir(self):
        return self.a / self.b

aritmetica1 = Aritmetica(5, 3)

print('Suma:', aritmetica1.sumar())
print('Resta:', aritmetica1.restar())
print('Multiplicación:', aritmetica1.multiplicar())
print(f'División: {aritmetica1.dividir():.2f}')