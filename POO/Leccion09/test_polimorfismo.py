from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalle(objeto):
    #print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalle())
    # Pregunta si el objeto es de tipo empleado y muestra el atributo departamento
    if isinstance(objeto, Gerente):
        print(objeto.departamento)

empleado = Empleado('Cristian', 10000)
imprimir_detalle(empleado)

gerente = Gerente('Stefhani', 20000, 'Sistema')
imprimir_detalle(gerente)