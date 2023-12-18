

# Leer una edad hasta que el usuario escribe una edad correcta 18 a 100

while True:
    
    # capturar ValueError: invalid literal for int() wiyh base 10: 'hola'
    try:
        edad = int(input('Introduce tu edad (18 -100):'))
    
        if 18 <= edad <= 100:
            print('Edad correcta.')
            break
    
    except ValueError:
        print('FOrmato de datos incorrecto')
        
        
        # Leer un booleano hasta que este bien escrito
        