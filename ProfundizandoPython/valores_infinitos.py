# valor mas grande en positivo y valor mas grande en negativo
import math
from decimal import Decimal
print(f'Utilizando float'.center(50, '-'))
infinito_positivo = float('inf')
print(f'Infinito positivo: {infinito_positivo}')
print(f'Es infinito?: {math.isinf(infinito_positivo)}')

infinito_negativo = float('-inf')
print(f'Infinito negativo: {infinito_negativo}')
print(f'Es infinito? {math.isinf(infinito_negativo)}')

# infinitos con la clase math
print(f'Con la función math'.center(50, '-'))
infinito_positivo = math.inf
print(f'Infinito positivo: {infinito_positivo}')
print(f'Es infinito?: {math.isinf(infinito_positivo)}')

infinito_negativo = -math.inf
print(f'Infinito negativo: {infinito_negativo}')
print(f'Es infinito? {math.isinf(infinito_negativo)}')

# Utilizando el modulo Decimal
print(f'Utilizando decimal'.center(50, '-'))
infinito_positivo = Decimal('Infinity')
print(f'Infinito positivo: {infinito_positivo}')
print(f'Es infinito?: {Decimal.is_infinite(infinito_positivo)}')

infinito_negativo = -Decimal('Infinity')
print(f'Infinito negativo: {infinito_negativo}')
print(f'Es infinito? {Decimal.is_infinite(infinito_negativo)}')
