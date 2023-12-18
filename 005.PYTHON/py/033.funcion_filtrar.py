
# lista de precios
# filtrar precios por rango
"""
CREAR UNA FUNCION QUE RECIBA UNA LISTA DE PRECIOS, UN PRECIO MIN, UN PRECIO MAX
LA FUNCION DEBE COMPROBAR UNO A UNO LOS PRECIOS Y COMPROBAR SI ESTAN
COMPRENDIDOS ENTRE MIN Y PRECIO MAX, SI LO ESTAN ENTONCES SE GUARDAN 
EN UNA LISTA DE RESULTADOS Y FINALMENTE SE DEVUELVE LA LISTA DE RESULTADOS
"""

def filtrar_precios(precios, precio_min, precio_max):
    
    lista = [] # lista para almacenar precios filtrados.
    for precio in precios:
        
        if precio_min <= precio <= precio_max:
            
            lista.append(precio) # append permite agregar un elemento al final de la lista 
                                 # (en este caso: en la lista vacia creada al principio [])
    return lista


precios = [20.99, 42.33, 55.50, 90.77, 36.77, 47,89]

# parametros: lista precios, precio minimo, precio maximo
# precios-filtrados es una lista de resultados, de precios filtrados

precios_filtrados = filtrar_precios(precios, 30, 50)
print(f'precios_filtrados {precios_filtrados}')    