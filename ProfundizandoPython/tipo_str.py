from mi_clase import MiClase
# Profundizando en el tipo str
# Las str son inmutables, eso quiere decir que con cualquier cambio, cambia su direccion en memoria

# Forma de concatenacion automatica
variable = 'Adios'
mensaje = 'Hola' 'Mundo' + variable
print(f'Mensaje 1: {mensaje}, id: {id(mensaje)}')
mensaje += 'Universidad' 'Python'

c = mensaje.capitalize()
print(c)
#help(MiClase)
print(f'Mensaje 1: {mensaje}, id: {id(mensaje)}')
print(f'Mensaje 2: {c}, id: {id(c)}')

#Join se puede utilizar en cualquier valor iterable string, listas, tuplas y diccionarios
print(f'Uso de join'.center(50, '-'))
valores = ['ab', 'cd', 'fg', 'hi']
resultado = ', '.join(valores)
print(resultado)
print(f'Join con diccionarios'.center(50, '-'))
diccionario = {
    'nombre': 'Cristian',
    'apellido': 'Zelaya',
    'edad': '28'
}
llaves = '-'.join(diccionario.keys())
print(f'Llaves: {llaves}')
valores = '-'.join(diccionario.values())
print(f'Valores: {valores}')

print(f'Uso de split'.center(50, '-'))
valores = 'Hola-mundo-adios'
resultado = valores.split('-')
print(f'Resultado: {resultado}')
