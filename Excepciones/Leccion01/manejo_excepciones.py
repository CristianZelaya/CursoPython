from excepciones_personalizadas import NumerosIdenticosException

resultado = None

# Asi se crea un try except
try:
    a = int(input('a. Ingresa un valor numerico: '))
    b = int(input('b. Ingresa un valor numerico: '))
    if a == b:
        raise NumerosIdenticosException('Los numeros son identicos')
    resultado = a / b
except ZeroDivisionError as e:
    print(f'Ocurrio un error: {e}')
except TypeError as e:
    print(f'Ocurrio un error: {e}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
# Bloque de codigo opcional
else:
    print('No se arrojo ninguna excepcion')
finally:
    print('Se ejecuto el bloque finally')

print(f'Resultado: {resultado}')
print(f'Continuamos...')

# Exception es la clase padre para el manejo de errores
# Se puede tener mas de una excepcion