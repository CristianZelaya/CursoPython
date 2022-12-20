class Persona:

    contador_personas = 0

    # Mejora de codigo
    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas

    def __init__(self, nombre, apellido, edad):
        self.id_persona = self.generar_siguiente_valor()
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        return f'Persona[id: {self.id_persona}, nombre: {self.nombre}, apellido: {self.apellido}, edad: {self.edad}]'

persona = Persona('Cristian', 'Zelaya', '28')
print(persona)
persona2 = Persona('Stefhani', 'Gómez', 29)
print(persona2)