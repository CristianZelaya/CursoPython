class Empleado:
    def __init__(self, nombre, sueldo):
        self._nombre = nombre
        self._sueldo = sueldo


    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    def __str__(self):
        return f'Nombre: {self._nombre}, Sueldo: {self._sueldo}'

    # Polimorfismo, esta funcion se puede usar en clase padre y clase hija
    def mostrar_detalle(self):
        return self.__str__()

if __name__ == '__main__':
    empleado = Empleado('Cristian', 1500)
    print(empleado)