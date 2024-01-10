"""
Crear una lista de precios

En un bucle infinito imprimir un menu de opciones:
1 - Ver todos los precios
2 - Ver un precio por posición
3 - Crear un nuevo precio
4 - Actualizar un precio existente
5 - Borrar un precio exixtente
6 - Borrar todos los precios
7 - 
8 - salir
Para utilizar los metodos que estan en input_utils: read-int, read-bool
"""

from input_utils import read_int, read_float, read_bool

precios = [29.99, 44.32, 64.48]

print("""
Crear una lista de precios

En un bucle infinito imprimir un menu de opciones:
1 - Ver todos los precios
2 - Ver un precio por posición
3 - Crear un nuevo precio
4 - Actualizar un precio existente
5 - Borrar un precio exixtente
6 - Borrar todos los precios
7 - Eliminar los precios superiores a un número introducido por el usuario
8 - salir
""")
    
while True:
    opcion = read_int('Introduce la opción (1 a 8):')
    
    if opcion == 1:
        print('Ha elegido ver todos los precios: ')
        print(precios)
        
    elif opcion == 2:
        print('Ha elegido ver un precio en concreto')
        posicion = read_int('Introduce la posición del precio que desea consultar: ')
        if 1<= posicion <= len(precios):
            print( precios[posicion - 1]) # -1 adaptar al rango de 0 a len(precios)        
        else:
            print('posición incorrecta')
            
    elif opcion == 3:
        print('Ha elegido crear un nuevo precio')
        crear_precio = read_float('Introduce el nuevo precio: ')
        precios.append(crear_precio)
        
    elif opcion == 4:
        print('Ha elegido actualizar un precio existente')
        print(precios)
        posicion = read_int('Introduce la posicion del precio que desea modificar: ')
        if 1<= posicion <= len(precios):
            precio_modificado = read_float('Introduce precio modificado: ')       
            precios[posicion - 1] = precio_modificado
            
    elif opcion == 5:
        print('Ha elegido borrar un precio existente')
        print(precios)
        posicion = read_int('Introduce la posicion del precio que desea borrar: ')
        if 1<= posicion <= len(precios):
            precio_borrado = precios.pop(posicion - 1) 
            print(f'Precio borrado exitosamente: {precio_borrado}')
        else:
            print('posicion incorrecta')
    # Opción 2:
    # del precios[posicion -1]
    
    # Opcion 3:
    # precio_borrado = percios[posicion - 1]
    # precios.remove(precio_borrado)
    
    elif opcion == 6:
        print('Ha decidido eliminar todos los precios') # Vaciar el carrito
        confirmacion = read_bool('¿Esta seguro/a de vaciar el carrito (si/no): ')
        if confirmacion:
            # precios.clear()
            precios = []
            print(f'Carrito vacio {precios}')
        else:
            print('no se eliminarán los precios.') 
            
    elif opcion == 7: 
        max = read_float('Introduce el precio max: ')
        # IMPORTANTE: Borrar mientras se itera es problemático, genera inconsistencias, probar a depurar
        #for precio in precios:
        #   if precio >  max:
        #     precios.remove(precio)
        
        # Opcion 1:
        #precio_a_borrar = [] 
        #for precio in precios:
        #   if precio > max:
        #        precio_a_borrar.append(precio)
        #for precio in precio_a_borrar:
        #    precios.remove(precio)
        
        # Opcion 2: 
        precios = [precio for precio in precios if precio <= max] # Borrar elementos en una lineA
         
    elif opcion == 8:
        print('Saliendo de la app, nos vemos.')
        break
    else: 
        print('Opción incorrecta. Introduce un valor en el rango de 1 a 8')
           