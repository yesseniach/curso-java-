
# Operadores membresias
# Comprueban si un valor es miembro de una secuencia string o estructura de datos

# in con textos

print("java" in "curso avanzado de java con spring") # True
print("java" in "curso avanzado de python con Flask") # False

# in en listas
students = ['Jehiel','Judith', 'Yessi', 'Lily', 'Silvia']
name = input('Introduce tu nombre:')

if name in students:
    print('Tienes acceso al curso java.')
else:
    print('No eres VIP.')
    
# not in
if name not in students:
   print('No tienes acceso al curso java.') 