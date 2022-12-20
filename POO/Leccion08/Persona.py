class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other):
        return f'{self.nombre} {other.nombre}'

    def __sub__(self, other):
        return self.edad - other.edad


persona = Persona('Cristian', 28)
persona2 = Persona('Arnulfo', 20)

print(persona + persona2)
print(persona - persona2)
