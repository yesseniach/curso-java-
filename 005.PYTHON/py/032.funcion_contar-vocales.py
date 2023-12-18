
# devuelve el numero de vocales
def contar_vocales(texto):
    
    num_vocales = 0
    for letra in texto:
        # if caracter == 'a' or caracter == 'e' or caracter == ''= 
        if letra.lower() in 'aeiou':
            num_vocales += 1
            
    return num_vocales
    
        
    
resultado1 = contar_vocales('Alan')
print(f'resultado1 {resultado1}') #2

resultado2 = contar_vocales('Hola mundo')
print(f'resultado2 {resultado2}')  #4  