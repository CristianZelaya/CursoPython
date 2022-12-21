class Orden:

    contador_ordenes = 0

    def __init__(self, computadora):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._computadora = list(computadora)

    @property
    def computadura(self):
        return self._computadora

    @computadura.setter
    def computadora(self, computadora):
        self._computadora = computadora

    def agregar_computadora(self, computadora):
        self._computadora.append(computadora)

    def __str__(self):
        computadoras_str = ''
        for computadora in self._computadora:
            computadoras_str += computadora.__str__()
        return f'ID: {self._id_orden} \n{computadoras_str}'