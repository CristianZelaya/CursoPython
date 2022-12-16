from Persona import Persona

class Empleado(Persona):
    # Se heredan los campos usando la palabra super e igual se pasan en el metodo init
    def __init__(self, nombre, apellido, edad, sueldo):
        super().__init__(nombre, apellido, edad)
        self.sueldo = sueldo

    # Se hereda el metodo str de la clase padre
    def __str__(self):
        return f'{super().__str__()}, Sueldo: {self.sueldo}'