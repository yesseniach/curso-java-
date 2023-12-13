
coches = ['Mercedes', 'BMW', 'Skoda', 'Alfa Romeo', 'Maserati', 'Seat']

# sort() ordena de forma ASCENDENTE; de menos a mas A - Z
coches.sort()
print(coches)

# sort(reverse=True) ordena de forma DESCENDENTE, de mas a menos Z - A
coches.sort(reverse=True)
print(coches)

#Invirtiendo el orden de los elementos en torno al centro
# reverse() equivalente a .sort(reverse=True)
coches2 = ['Mercedes', 'BMW', 'Skoda', 'Alfa Romeo', 'Maserati', 'Seat']
coches2.reverse()
print(coches2)

# sorted() la diferencia es que este no modifica la original
# devuelve una nueva lista con los elementos ordenados
precios = [1.11, 2.22, 3.33, 7.77, 4.44, 6.66]
precios_asc = sorted(precios)
print(precios)
print(precios_asc)

# sorted(reverse=True)
calificaciones = [1.11, 2.22, 3.33, 7.77, 4.44, 6.66]
calificaciones_desc = sorted(calificaciones, reverse=True)
print(calificaciones_desc)

calificacion_maxima = calificaciones_desc[0] # EL primero
calificacion_minima = calificaciones_asc[-1] # el ultimo
# otre opcion para obtener el ultimo
last_index = len(calificaciones_desc) - 1
calificacion_minima = calificaciones_desc[last_index]