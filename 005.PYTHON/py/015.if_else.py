
# Estructuras de control condicional
precio = float(input('Introduce un precio:'))

if precio >= 100:
    print('El Producto es Caro')
elif  precio > 50:  # > 50 es normal
    print('Es Normal')
else: # es barato
    print('El Producto es muy Barato')
    
    
# RUtina Diaria 24 Horas

hora = int(input('Introduce la hora:'))

# 0 - 8 esta durmiendo
# 8 - 15 esta en clase de angular
# 15 a 16 esta comiendo
# 16 a 21 esta en clase de Java
# 21 a 24 esta cenando
# Si es mas de 24 entonces imprimir hora incorrecta
if 0<= hora < 8:
    print('Esta durmiendo 😴') # EMOJI tecla windows mas acento al lado de la P
elif 8 <= hora < 15:
    print('Esta en clase de Fronted 💻')
elif 15 <= hora < 16:
    print('Esta comiendo 🍝')
elif 16 <= hora < 21:
    print('Esta en clase de Java 💻')
elif 21 <= hora < 24:
    print('Esta cenando 🥗')
else:
    print('Introduce hora correcta')