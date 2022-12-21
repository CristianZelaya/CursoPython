class Monitor:

    contador_monitores = 0

    def __init__(self, marca, tamano):
        Monitor.contador_monitores += 1
        self._id_monitor = Monitor.contador_monitores
        self._marca = marca
        self._tamano = tamano

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def tamano(self):
        return self._tamano

    @tamano.setter
    def tamano(self, tamano):
        self._tamano = tamano

    def __str__(self):
        return f'Monitor -> ID: {self._id_monitor} | Marca: {self._marca} | Tamaño: {self._tamano}'

if __name__ == '__main__':

    monitor = Monitor('Lenovo', '24"')
    print(monitor)
    monitor2 = Monitor('Sony', '32"')
    print(monitor2)