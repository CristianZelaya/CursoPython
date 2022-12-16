from Persona import Persona
class Empleado(Persona):
    def __init__(self, nombre, apellido, edad, sueldo):
        super().__init__(nombre, apellido, edad)
        self.sueldo = sueldo

empleado = Empleado('Cristian', 'Zelaya', 28, 5000)
print(empleado.nombre)