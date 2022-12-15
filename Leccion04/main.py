"""# Ciclo While
contador = 0
while contador < 3:
    print(f'Contador = {contador}')
    contador += 1
else:
    print('Fin del ciclo while')"""

"""# While creciente
max = 5
num = 0
while num <= max:
    print(f'Número: {num}')
    num += 1
else:
    print('Fin del ciclo')"""

"""# While decreciente
min = 1
num = 5
while min <= num:
    print(f'Número: {num}')
    num -= 1
else:
    print('Fin del ciclo')"""

"""#Ciclo for
cadena = 'Hola'
for letra in cadena:
    print(letra)
else:
    print('Fin ciclo for')"""

# Palabra Break

"""palabra = 'Holanda'
for letra in palabra:
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
        break
else:
    print('Fin del ciclo for')"""

# Palabra continue

for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor: {i}')