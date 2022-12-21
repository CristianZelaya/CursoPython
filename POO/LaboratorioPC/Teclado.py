from DispositivoEntrada import DispositivoEntrada


class Teclado(DispositivoEntrada):

    contador_teclados = 0

    def __init__(self, tipo, marca):
        Teclado.contador_teclados += 1
        self._id_teclado = Teclado.contador_teclados
        super().__init__(tipo, marca)

    def __str__(self):
        return f'ID: {self._id_teclado} | {super().__str__()}'

if __name__ == '__main__':

    tipo = 'Teclado'
    teclado = Teclado(tipo, 'Lenovo')
    teclado2 = Teclado(tipo, 'Asus')
    print(teclado)
    print(teclado2)
