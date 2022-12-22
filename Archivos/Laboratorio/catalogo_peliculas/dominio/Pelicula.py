class Pelicula():

    contador_peliculas = 0
    def __init__(self, nombre):
        Pelicula.contador_peliculas += 1
        self.id_pelicula = Pelicula.contador_peliculas
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f'Id: {self.id_pelicula} | Nombre: {self._nombre}'

# Probando la clase
if __name__ == '__main__':
    pelicula = Pelicula('Spiderman')
    print(pelicula)