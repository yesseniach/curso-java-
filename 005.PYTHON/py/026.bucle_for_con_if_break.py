# vehiculos = ['Mercedes', 'lambo', 'Tractor John Deere', 'Bici Orbea', 'Patinete']

# Iterar con bucle for y si el vehiculo contiene "tractor" entonces imprimir y salir
# entonces imprimir y salir del bucle

vehiculos = ['Mercedes', 'lambo', 'Tractor John Deere', 'Bici Orbea', 'Patinete']

for vehiculo in vehiculos:
    if 'tractor' in vehiculo.lower():
        print(f'tractor encontrado: {vehiculo}')
        break