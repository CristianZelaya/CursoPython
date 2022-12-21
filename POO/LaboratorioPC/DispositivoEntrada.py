class DispositivoEntrada():

    def __init__(self, tipo, marca):
        self._tipo = tipo
        self._marca = marca

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self.tipo = tipo

    @property
    def marca(self):
        return self._marca

    @tipo.setter
    def marca(self, marca):
        self._marca = marca

    def __str__(self):
        return f'Dispositivo de entrada -> Tipo: {self._tipo} | Marca: {self._marca}'

if __name__ == '__main__':
    dispositivo = Dispositivo_Entrada('Raton', 'Lenovo')
    print(dispositivo)
    print(dispositivo.tipo)
    print(dispositivo.marca)