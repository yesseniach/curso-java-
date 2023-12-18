
vehiculos = ['mercedes rojo', 'bmw gris', 'tractor azul', 'tractor rosa', 'patinete azul']

# hacer un bucle for que itere imprimiendo cada vehiculo y si es de
# color azul salta a la siguiente iteracion
# usar continue

for vehiculo in vehiculos:
    if 'azul' in vehiculo.lower():
        continue
    
    print(vehiculo) # solo imprime si el vehiculo no es azul
# a diferencia de break que rompe el bucle,
#continue se mantiene dentro pero salta a la siguiente iteracion
    

    