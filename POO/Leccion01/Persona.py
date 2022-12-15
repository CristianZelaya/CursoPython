"""class Persona:
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos

    def mostrar_detalle(self):
        print(f'Nombre: {self.nombre} Apellido: {self.apellido} Edad: {self.edad} Tupla: {self.valores} Diccionario: {self.terminos}')

persona1 = Persona('Cristian', 'Zelaya', 28, 2, 3, 4, 5, m='Manzana', p='Pera')
#print('Persona 1: ', persona1.nombre, persona1.apellido, persona1.edad)
persona2 = Persona('Stefhani', 'Gómez', 28)
#print('Persona 2: ', persona2.nombre, persona2.apellido, persona2.edad)

persona1.mostrar_detalle()
persona2.mostrar_detalle()"""

"""# Cambiar valores de un objeto
persona1.nombre = 'Arnulfo'
persona1.apellido = 'Ventura'
persona1.edad = 27
print('Persona 1: ', persona1.nombre, persona1.apellido, persona1.edad)"""

# Encapsulamiento
""""
get: obtener/recuperar
set: colocar/modificar
"""
class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    # Metodo get
    @property
    def nombre(self):
        return self._nombre

    # Metodo set
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def mostrar_detalle(self):
        print(f'Nombre: {self._nombre} Apellido: {self._apellido} Edad: {self._edad}')

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    # Para eliminar un objetos 'Destructor'
    def __del__(self):
        print(f'Persona: {self._nombre} {self._apellido}')

# Este codigo solo se ejecuta directamente de este archivo, no de un modulo o archivo externo
if __name__ == '__main__':
    persona1 = Persona('Cristian', 'Zelaya', 28)
    persona1.mostrar_detalle()
    persona1.nombre = 'Arnulfo'
    persona1.apellido = 'Ventura'
    persona1.edad = 27
    print('Valores modificados')
    persona1.mostrar_detalle()
    print(__name__)

# Cuando solo hay metodo get se conoce como variable de solo lectura
# Modulos utilizar la clase en otro archivo
# Destructores de python, cuando se elimina un objeto de manera explicita