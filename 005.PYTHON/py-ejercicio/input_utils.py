"""
Archivo con funciones de utilidad para leervdatos por consola
utilizando input, while, try, execept
"""

def read_int(prompt):
    while True:
        try: 
            numero = int(input(prompt)) # devuelve el valor leido por consola
            return numero
        except Exception:
            print('No se ha podido leer el numero int')
                  
                  
edad = read_int('Introduce tu edad')
peso = read_int('Introduce tu peso')
altura = read_int('Introduce tu altura')




def read_float(prompt):
    while True:
        try: 
            numero = float(input(prompt)) # devuelve el valor leido por consola
            return numero
        except Exception:
            print('No se ha podido leer el numero float')
                  
                  
edad = read_float('Introduce tu edad')
peso = read_float('Introduce tu peso')
altura = read_float('Introduce tu altura')