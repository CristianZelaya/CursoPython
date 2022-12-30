import math
from decimal import Decimal

print('Utilizando float'.center(50, '-'))
# NaN - Not a number (no es un numero)
# NaN no es sensible a mayusculas/minusculas
# NaN es un tipo de dato numerico indefinido

a = float('NaN')
print(f'a: {a}')
print(f'Es NaN (not a number): {math.isnan(a)}')

print(f'Utilizando Decimal'.center(50, '-'))
a = Decimal('NaN')
print(f'a: {a}')
print(f'Es NaN (not a number): {Decimal.is_nan(a)}')

