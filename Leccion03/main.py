"""print('---Sentencias de Control---')

condicion = 'Hola'
if condicion == True:
    print('La condicion es Verdadera')
elif condicion == False:
    print('La condicion es falsa')
else:
    print('Condicion no reconocida')"""

"""print('---Convertir numero---')
num = int(input('Inserte un numero (1 al 3): '))
numeroTexto = ''
if num == 1:
  numeroTexto = 'número "uno"'
elif num == 2:
    numeroTexto = 'número "dos"'
elif num == 3:
    numeroTexto = 'número "tres"'
else:
    numeroTexto = 'El número no es valido'
print(f'Número proporcionado: {num} => {numeroTexto}')"""

"""# Operador ternanrio
condicion = False
print('Condicion verdadera') if condicion else print('Condicion falsa')"""

"""mes = int(input('Proporciona mes del año (1-12): '))
estacion = None

if mes == 1 or mes == 2 or mes == 12:
    estacion = 'Invierno'
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'Primavera'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Verano'
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'Otoño'
else:
    estacion = 'Mes incorrecto'

print(f'Para el mes {mes} la estación es: {estacion}')"""

"""edad = int(input('Proporciona tú edad: '))
mensaje = None
if 0 <= edad < 10:
    mensaje = 'La infancia es increíble...'
elif 10 <= edad < 20:
    mensaje = 'Muchos cambios y mucho estudio...'
elif 20 <= edad < 30:
    mensaje = 'Amor y comienza el trabajo...'
else:
    mensaje = 'Estapa de la vida no reconocida'
print(f'Tú edad es: {edad}, {mensaje}')"""

# Notas

nota = int(input('Proporciona tú nota (1 al 10): '))

mensaje = None
if nota > 10 or nota < 0:
    mensaje = 'Proporciona una nota correcta'
elif nota > 8:
    mensaje = 'A'
elif nota == 8:
    mensaje = 'B'
elif nota == 7:
    mensaje = 'C'
elif nota == 6:
    mensaje = 'D'
else:
    mensaje = 'F'
print(f'Tú nota es: {nota} => {mensaje}')
