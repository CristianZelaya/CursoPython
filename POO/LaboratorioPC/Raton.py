from DispositivoEntrada import DispositivoEntrada


class Raton(DispositivoEntrada):

    contador_ratones = 0

    def __init__(self, tipo, marca):
        Raton.contador_ratones += 1
        self.id_raton = Raton.contador_ratones
        super().__init__(tipo, marca)

    def __str__(self):
        return f'ID: {self.id_raton} | {super().__str__()}\n'

if __name__ == '__main__':

    tipo = 'Raton'
    raton = Raton(tipo, 'Lenovo')
    raton2 = Raton(tipo, 'Hp')
    print(raton)
    print(raton2)
