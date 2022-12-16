class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        return f'Persona: Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}'