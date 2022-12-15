# Enviar un saludo a al consola utilizando pithon
# print("Este es mi saludo desde python...")
name = 'Cristian Zelaya'
cellphone = 70835249
email = 'criszel94@gmail.com'

print(name)
print(cellphone)
print(email)

# Tipos de datos
# int
x = 10
print(type(x))

# float
x = 10.5
print(type(x))

# Boolean
x = True
print(type(x))
x = False
print(type(x))

# String
x = 'Hello World'
print(type(x))

print('---------------')
miEquipoFavorito = 'F.C. Barcelona'
comentario = 'El mejor equipo del mundo'

# print('Mi equipo favorito es: ' + miEquipoFavorito + ' ' + comentario)

print('Mi equipo favorito es:', miEquipoFavorito, comentario)

# Pasar cadena de numero a enteros

x = '12'
y = '2'
# Funcion int pasa el valor a entero
z = int(x) + int(y)
print('Suma:', z)

# Tipo Boolean

print('-----Boolean-----')

miVariable = True
print(miVariable)

print('-----------')

miVariable = 3 > 2
print(miVariable)

if miVariable:
    print('El resultado es verdadero')
else:
    print('El resultado es falso')


#Utilizando funcion imput

#resultado = input('Escribe un mensaje: ')

#num1 = int(input('Escribe el primer numero: '))
#num2 = int(input('Escribe el segundo numero: '))
#resultado = num1 + num2
#print('La suma es:', resultado)

"""valorDia = int(input('Como estuvo tu día (1 al 10): '))
if valorDia < 3:
    print('MALO:', valorDia)
elif valorDia < 6:
    print('REGULAR:', valorDia)
elif valorDia < 8:
    print('BIEN:', valorDia)
else:
    print('EXCELENTE', valorDia)

print('Fin del programa')"""

titulo = input('Proporciona el titulo del libro: ')
autor = input('Proporciona el autor del libro: ')

print(titulo, 'fue escrito por', autor)
