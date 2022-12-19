from abc import ABC,abstractmethod

# Se convirtio a una clase abstracta
class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        # Validacion
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor erroneo de ancho: {ancho}')
        if 0 < self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = alto
            print(f'Valor erroneo de alto: {alto}')

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f'Valor erroneo {ancho}')

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f'Valor erroneo: {alto}')

    @abstractmethod
    def calcular_area(self):
        pass

    def __str__(self):
        return f'El ancho es: {self._ancho}, El alto es: {self._alto}'

    # funcion para validar que el valor este en el rango de 1 a 10
    def _validar_valor(self, valor):
        return True if 0 < valor < 10 else False
