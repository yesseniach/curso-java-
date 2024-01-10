from input_utils import read_int, read_float, read_bool


precios = [29.99, 44.32, 64.48]

print("""
Elige una opción:
1 - Ver todos los precios
2 - Ver un precio por posición
3 - Crear un nuevo precio
4 - Actualizar un precio existente
5 - Borrar un precio exixtente
6 - Borrar todos los precios
7 - Eliminar los precios superiores a un número introducido por el usuario
8 - salir
""")
def ver_precios(precios):
    print('Ha elegido ver todos los precios')
    print(precios)    


def un_precio(precios):
    global precios # UTILIZA LA VARIABLE global precios
    print('Ha elegido ver un precio en concreto')
    posicion = read_int('Introduce la posición del precio que desea consultar: ')
    if 1<= posicion <= len(precios):
        print( precios[posicion - 1]) # -1 adaptar al rango de 0 a len(precios)        
    else:
        print('posición incorrecta')

def crear_precio(precios):
    print('Ha elegido crear un nuevo precio')
    crear_precio = read_float('Introduce el nuevo precio: ')
    precios.append(crear_precio)

def actualizar_precio(precios):
    print('Ha elegido actualizar un precio existente')
    print(precios)
    posicion = read_int('Introduce la posicion del precio que desea modificar: ')
    if 1<= posicion <= len(precios):
        precio_modificado = read_float('Introduce precio modificado: ')       
        precios[posicion - 1] = precio_modificado

def borrar_precio(precios):
    print('Ha elegido borrar un precio existente')
    print(precios)
    posicion = read_int('Introduce la posicion del precio que desea borrar: ')
    if 1<= posicion <= len(precios):
        precio_borrado = precios.pop(posicion - 1) 
        print(f'Precio borrado exitosamente: {precio_borrado}')
    else:
        print('posicion incorrecta')

def vaciar_carrito():
    print('Ha decidido eliminar todos los precios') # Vaciar el carrito
    confirmacion = read_bool('¿Esta seguro/a de vaciar el carrito (si/no): ')
    if confirmacion:
            # precios.clear()
        precios = []
        print(f'Carrito vacio {precios}')
    else:
        print('no se eliminarán los precios.')
    return precios

def max_precio(precios):
                # indica a python que use la lista precios externa global en vez de crear una local
    max = read_float('Introduce el precio max: ')
    precio_a_borrar = [] 
    for precio in precios:
       if precio > max:
           precio_a_borrar.append(precio)
    for precio in precio_a_borrar:
        precios.remove(precio)

while True:
    opcion = read_int('Introduce la opción (1 a 8):')
    
    if opcion == 1:
        ver_precios(precios)
        
    elif opcion == 2:
        un_precio(precios)
            
    elif opcion == 3:
        crear_precio(precios)
        
    elif opcion == 4:
        actualizar_precio(precios)
            
    elif opcion == 5:
        borrar_precio(precios)
       
    elif opcion == 6:
        precios = vaciar_carrito() 
            
    elif opcion == 7: 
        max_precio(precios)
        
    elif opcion == 8:
        print('Saliendo de la app, nos vemos.')
        break
    else: 
        print('Opción incorrecta. Introduce un valor en el rango de 1 a 8')
           