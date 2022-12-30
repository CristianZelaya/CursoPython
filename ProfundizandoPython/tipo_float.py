# Profundizando en el tipo float
a = 3.0

# :.2f da formato y muestra dos numero despues del punto
# cuando se pasan varios tipos de datos validos al contructor se llama sobrecarga

a = float(10)
a = float('10')

#Notacion exponenencial (valores positivos o negativos)

a = 3e12
print(f'a: {a:.2f}')

a = 3e-5
print(f'a: {a:.10f}')

# Cualquier calculo de flotante se converte en flotante
a = 4.0 + 5
print(f'a: {a}')
