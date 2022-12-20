class Persona:

    contador_personas = 0

    def __init__(self, nombre, apellido, edad):
        Persona.contador_personas += 1
        self.id_persona = Persona.contador_personas
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        return f'Persona[id: {self.id_persona}, nombre: {self.nombre}, apellido: {self.apellido}, edad: {self.edad}]'

persona = Persona('Cristian', 'Zelaya', '28')
print(persona)
persona2 = Persona('Stefhani', 'Gómez', 29)
print(persona2)