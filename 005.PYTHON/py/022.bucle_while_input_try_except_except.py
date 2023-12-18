
vehiculos = ['Mercedes', 'lambo', 'Tractor John Deere', 'Bici Orbea', 'Patinete']

while True:
    
    try:
    
        indice = int(input(f'Introduzca que vehiculo desea hoy (0 a {len(vehiculos) - 1})'))
        vehiculo = vehiculos[indice]
        print(f'Excelente decision, ha elegido el vehiculo {indice}: {vehiculo}')
        break

    # IndexError: list index out of range
    # ValueError: invalid literal for int() white base 10:'hola'
    except IndexError as e:
        print(f"Se ha producido un error de acceso por índice incorrecto: {e}")
    except ValueError as e:
        print(f"Se ha producido un error de formato de dato incorrecto: {e}")