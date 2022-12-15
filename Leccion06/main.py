"""# Funciones en python
def miFuncion(nombre, apellido):
    print(nombre, apellido)

miFuncion('Cristian', 'Zelaya')"""

"""def sumar(a, b):
    return a + b

resultado = sumar(10, 5)
print(resultado)"""

"""# Agregar valores por default
def sumar(a = 0, b = 0):
    return a + b
print(f'Resultado sumar: {sumar(2, 8)}')"""

"""# pasar argumentos variables
def listarDatosUsuario(*datos):
    for dato in datos:
        print(dato)
listarDatosUsuario('Cristia', 'Zelaya', 28, 75464859)"""

"""# Ejercicio suma
def sumar(*args):
    resultado = 0
    for valor in args:
        resultado += valor
    print(resultado)
sumar(2, 4, 5, 8, 10)"""

"""# Ejercicio multiplica
def multiplicar(*args):
    resultado = 1
    for valor in args:
        resultado *= valor
    return resultado
print(multiplicar(3, 5, 15))"""

"""# Pasar un diccionario en una funcion
def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')
listarTerminos(nombre='Cristian', apellido='Zelaya', cel=70835249, id=1)"""

"""# Diferentes tipos de datos, una lista
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres = ['Cristian', 'David', 'Stefhani', 'Josué']
desplegarNombres(nombres)
# Pasar tupla
desplegarNombres((10, 11))
# Pasar listas
desplegarNombres([12, 13])"""

"""# Funciones recursivas es una funcion que se manda a llamar asi misma, para cumplir una funcion
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)
numero = 10
resultado = factorial(numero)
print(f'El factorial de {numero} es {resultado}')"""

"""# Ejercicio
def cuentaRegresiva(numero):
    if numero >= 1:
        print(numero)
        cuentaRegresiva(numero - 1)
    elif numero == 0:
        return
    else numero <0:
        print('Valor incorrecto')
cuentaRegresiva(5)"""

"""# Calculadora de impuestos
def calcularPago(pago, impuesto):
    total = pago + pago * (impuesto/100)
    print(f'Pago con impuesto: {total}')

pago = float(input('Proporcione el pago sin impuesto: '))
impuesto = float(input('Proporcione el monto del impuesto: '))

calcularPago(pago, impuesto)"""

# Celcios a Faren

"""def init():
    print(f'''
        --- Bienvenido, elige una opcion ---
        1. Convertir Celsius a Farenheit
        2. Convertir Farenheit a Celsius
    ''')

    opcion = int(input('Escribe la opción: '))

    resultado = 0
    if opcion == 1:
        print('Elegiste convertir celsius a farenheit')
        celsius = float(input('Grados celsius: '))
        resultado = (celsius * 9/5) + 32
        print(f'{celsius}°C es igual a: {resultado:.2f}°F')
    elif opcion == 2:
        print('Elegiste convertir farenheit a celsius')
        farenheit = float(input('Grados farenheit: '))
        resultado = (farenheit - 32) * (5/9)
        print(f'{farenheit}°F es igual a: {resultado:.2f}°C')
    else:
        print('No es una opción valida')

init()"""