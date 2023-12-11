
edad = 30
peso = 80.34

print(edad + 2)
print(peso - 5)

#utilizando constructor
edad2 = int(40) #int es para números enteros
peso2 = float(90.55) #float es para decimales
print(edad2 + 2)
print(peso2 -5)

## convertir de texto a número
edad3 = "70"
peso3 = "100.21"
#TypeError: can only concatenate str (not "int") to str
#print(edad3 + 2)
#print(peso3 -5)

edad3_num = int(edad3) #convertir el texto "70" a número 70
print(edad3_num +2)

peso3_num = float(peso3) #convertir el texto "100.21" a número 100.21
print(peso3_num -5)

## convertir de número a texto
codigo_postal = str(28003) #convertir de int a str
print(codigo_postal)