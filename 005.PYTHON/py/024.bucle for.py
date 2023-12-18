

vehiculos = ['Mercedes', 'lambo', 'Tractor John Deere', 'Bici Orbea', 'Patinete']

# iterar sobre elementos
for vehiculo in vehiculos:
    print(vehiculo)


# iterar sobre indices utilizando la funcion range()
for index in range(0, 5, 1):
    print(vehiculos[index])
    
for index in range(5): 
    print(vehiculos[index])
    
for index in range(len(vehiculos)): 
    print(vehiculos[index])
    
coches = ['BMW','Mercedes','Seat','KIA','Honda']
for index in range(len(coches)):
    print(index, coches[index])
   