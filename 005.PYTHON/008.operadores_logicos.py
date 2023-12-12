
# and (AND) Y
# Restrictivo porque se tienen que cumplir todas
# las condiciones para que sea True

email_correcto = 'admin@gmail.com'
password_correcta = '1234'

email = input('Introduce tu email:')
password = input('Introduce password')

if email == email_correcto and password == password_correcta:
    print('Credenciales correctas')
else:
    print('Credenciales incorrectas')

# or 0
# Flexible porque es True si al menos se cumple
# na condicion

es_estudiante = input('Es estudiante? si o no ') == 'si' # True o False
precio = float(input('Introduce el precio de tu compra: '))

if es_estudiante or precio >= 100:
    print(f'Descuento del 20%, precio final: {precio * 0.80}')
else:
    print(f'Precio final: {precio}')   
