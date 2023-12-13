

texto = "Hola curso Java"

# len() calcular la longitud de un texto y de una estructura de datos
print(len(texto))

# upper() convierte a mayúsculas
print(texto.upper()) # nombre de la variable, punto y sale el metodo

# lower() convierte a minúsculas
print(texto.lower())

# capitalize() convierte sola la primera letra de todo el string a mayúscula
print(texto.capitalize())

# split() divide el texto en funcion de un separador, devuelve una lista
palabras = texto.split() # si no ponemos nada dentro de split() entonces separa por espacios
print(palabras) # ['Hola', 'curso', 'java']
print(palabras[0]) # Hola
print(palabras[1]) # curso
print(palabras[2]) # Java
# print(palabras[3]) # IndexError: list index out of range


texto_capitalized = palabras[0].capitalize() + " " + palabras[1].capitalize() + " " + palabras[2].capitalize()
print(texto_capitalized)
print(palabras[0].capitalize(), palabras[1].capitalize(), palabras[2].capitalize())

# format {} {} {} 
mensaje = "Hola curso {} la minima es de {} puntos."
print(mensaje.format("Java", 5))
print(mensaje.format("Python", 5))
print(mensaje.format("Spring", 7))

# format {} {} {} con tres huecos
plantilla = "{} {} {}"
texto_capitalized = plantilla.format(
 palabras[0].capitalize(),
 palabras[1].capitalize(), 
 palabras[2].capitalize()  
)
print(texto_capitalized)
    
# f strings
producto = "Lapto ASUS"
precio = 499.99
print(f"El producto seleccionado es {producto} con precio {precio} euros.")


# replace(x, y) reemplazas las ocurrencias del primer valor por el segundo valor
texto.replace
print(texto.replace('Java', 'Python'))
print("alan sastre".replace(" ","")) # Reemplaza todos los espacios
