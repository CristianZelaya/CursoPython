class MiClase:
    variableClase = 'Valor variable clase'

    def __init__(self, variableInstanacia):
        self.variableInstancia = variableInstanacia

    # Metodos estaticos
    @staticmethod
    def metodo_estatico():
        # Se puede acceder a la variable de clase de forma indirecta
        print(MiClase.variableClase)

    # Metodo de clase
    @classmethod
    def metodo_clase(cls):
        print(cls.variableClase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variableInstancia)
        print(self.variableClase)

print(MiClase.variableClase)

miClase = MiClase('Valor variable de instancia')
print(miClase.variableInstancia)
MiClase.metodo_estatico()
print('Metodo de clase'.center(50, '-'))
MiClase.metodo_clase()
print('Metodo de instancia'.center(50, '-'))
miClase.metodo_instancia()

# El contexto dinamico si puede acceder al contexto estatico
# En cambio el contexto estatico no puede acceder al contexto dinamico