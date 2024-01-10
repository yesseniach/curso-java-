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
                  
                  

def read_float(prompt):
    while True:
        try: 
            numero = float(input(prompt)) # devuelve el valor leido por consola
            return numero
        except Exception:
            print('No se ha podido leer el numero float')
   
   
                        
def read_bool(prompt):
   # respuesta = input(prompt)
   # booleano = respuesta.lower() in ['si', 'yes', 'sí']
   # return booleana # True o False
    while True:
        
            resultado = input(prompt).lower()# devuelve el valor leido por consola
            if resultado == 'si':
                return True
            elif resultado == 'no':
                return False
            else:
                print('Valor incorrecto')
                # no te saca del bucle, repite otra iteracion
            
                  
                  
# edad = read_int('Introduce tu edad: ')
# peso = read_int('Introduce tu peso: ')
# altura = read_int('Introduce tu altura: ')                 
# salario = read_float('introduce salario: ')                 
# activo = read_bool('Introduce si es trabajador por cuenta ajena (si/no): ')
# print(f'activo {activo}')