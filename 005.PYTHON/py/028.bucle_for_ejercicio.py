
# Lista de estudianres con respectivas notas
# numero_aprobados
# numero-suspensos
# porcentaje de aprobado


calificaciones = [
    'Miguel 5',
    'Allison 9',
    'Antonio 6',
    'Alan 3',
    'Patricia 4',
    'Bob 7',
    'Leyla 8'
    ]
num_aprobados = 0
num_suspensos = 0

for calificacion in calificaciones:
    # calificacion_partes = calificacion.split()
    # print(calificacion_partes[0])
    # print(calificacion_partes[1])
    # nota = int(calificacion_partes[1])
        # equivalente
    nota = int(calificacion.split()[1])
     
    if nota >= 5:
         num_aprobados += 1
    else:
         num_suspensos += 1
    
# imprimir numero aprobados y numero suspensos y porcentaje de aprobados redondeado a 2 decimales usando f string
num_total = len(calificaciones)
# num_total = num_aprobados + num_suspensos
porcentaje_aprobados =  round((num_aprobados / num_total) * 100, 2)

print(f'Número aprobados: {num_aprobados}')
print(f'Número suspensos: {num_suspensos}')
print(f'% de aprobados: {porcentaje_aprobados} %')
