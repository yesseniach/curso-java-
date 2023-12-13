
numero = -10
numero_absoluto = None

# if else normal

if numero <= 0:
    numero_absoluto = -numero
else:
    numero_absoluto = numero
    
print(numero_absoluto)


# operador ternario: if else en una linea
numero_absoluto = -numero if numero <= 0 else numero

# RECOMENDACION: usarlo solo en casos sencillos para evitar que la
# sentencia se vuelva muy compleja

## Otras opciones: Opcion 1 - nativa abs(), Opcion 2 - buscar er numpy