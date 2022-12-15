"""operandoA = int(input('Ingresa el valor A: '))
operandoB = int(input('Ingresa el valor B: '))

suma = operandoA + operandoB

# print('La suma es: ', suma)
# Imprimir con formato
print(f'La suma es: {suma}')

resta = operandoA - operandoB
print(f'La resta es: {resta}')

multi = operandoA * operandoB
print(f'La multiplicación es: {multi}')

division = operandoA / operandoB
print(f'La division es: {division}')

# Division entera
division = operandoA // operandoB
print(f'El division es (int): {division}')

# Residuo
residuo = operandoA % operandoB
print(f'El residuo es: {residuo}')

# Exponente
exponete = operandoA ** operandoB
print(f'El resultado exponente es: {exponete}')"""

"""alto = int(input('Ingresa el alto: '))
ancho = int(input('Ingresa el ancho: '))

area = alto * ancho
perimetro = (alto + ancho) * 2

print('El area es:', area)
print('El perimetro es:', perimetro)"""

# Asignacion
mivariable = 10
print(mivariable)

# Incremento con Reasignacion
mivariable += 1
print(mivariable)

print('----Operadores de comparacion----')

a = 4
b = 2

resultado = (a == b)
print(f'Resultado ==: {resultado}')

resultado = (a != b)
print(f'Resultado !=: {resultado}')

resultado = a > b
print(f'Resultado >: {resultado}')

resultado = a < b
print(f'Resultado <: {resultado}')

resultado = a >= b
print(f'Resultado >=: {resultado}')

resultado = a <= b
print(f'Resultado <=: {resultado}')

"""print('--------Par o Impar---------')

numero = int(input('Ingrese un numero: '))
if numero % 2 == 0:
    print(f'El numero {numero} es par')
else:
    print(f'El numero {numero} es impar')"""

"""print('--- Mayor de edad ---')

edad = int(input('Ingresa tu edad: '))

if edad >= 60:
    print(f'Eres un adulto mayor, tu edad es: {edad}')
elif edad >= 35:
    print(f'Eres un adulto, tu edad es: {edad}')
elif edad >= 18:
    print(f'Eres un adulto joven, tu edad es: {edad}')
elif edad >= 15:
    print(f'Eres un adolecente, tu edad es: {edad}')
elif edad > 0:
    print(f'Eres un niño, tu edad es: {edad}')
else:
    print('Ingresa una edad valida')"""

"""print('--- Operadores Logicos ---')

a = True
b = False

resultado = a and b
print(f'El resultado and es: {resultado}')

resultado = a or b
print(f'El resultado de or es: {resultado}')

resultado = not a
print(f'El resultado de not es: {resultado}')"""

"""print('--- Rango ---')

valor = int(input('Escribe un valor: '))
valorMin = 0
valorMax = 5

dentroRango = (valor >= valorMin) and (valor <= valorMax)

if dentroRango:
    print(f'{valor} esta dentro del rango')
else:
    print(f'{valor} no esta dentro del rango')"""

"""print('--- Asistir al juego ---')
vacaciones = False
diaDescanso = True

asistirAljuego = not (vacaciones or diaDescanso)

if asistirAljuego:
    print('No puede a sistir al juego, tiene deberes por hacer!')
else:
    print('Si puede asistir al juego')"""


"""edad = int(input('Introduce tu edad: '))
veintes = (edad >= 20 and edad < 30)
treintas = (edad >=20 and edad <40)

if veintes or treintas:
    if veintes:
        print("Dentro de los 20's")
    else:
        print("Dentro de los 30's")
else:
    print('Estas fuera de rango')"""

"""edad = int(input('Introduce tu edad: '))
if (20 <= edad < 30) or (30 <= edad < 40):
    print('Esta dentro del rango permitido')
else:
    print('Esta fuera del rango permitido')"""

"""num1 = int(input('Introduce nun1: : '))
num2 = int(input('Introduce nun2: '))
if num1 > num2:
    print(f'El num1 es mayor: {num1}')
else:
    print(f'El num2 es mayor: {num2}')"""

print('Proporcione los siguientes datos del libro')
name = input('Introduce el nombre del libro: ')
id = input('Introduce el ID del libro: ')
price = float(input('Introduce el precio del libro: '))
envio = input('El envio es gratuito? (True/False): ')

if envio == 'True':
    envio = True
    print(f'''
        Nombre: {name}
        Id: {id}
        Precio: ${price}
        Envio Gratuito?: {envio}''')
elif envio == 'False':
    envio = False
    print(f'''
        Nombre: {name}
        Id: {id}
        Precio: ${price}
        Envio Gratuito?: {envio}''')
else:
    print('Debe escribir un valor True/False')