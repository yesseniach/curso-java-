
# Borrar elementos de una lista existente

phones = ['666555444', '777666555', '656777454', '721453923']

# remove() borra un elemento que pasemos por parametro
phones.remove('777666555')
print(phones)

# pop() elimina y devuelve el ultimo elemento de la lista por su indice
# SI NO SE ESPECIFICA UN INDICE EN POP() POR DEFECTO TOMA EL ULTIMO ELEMENTO
pendientes_calificacion = ['Aitor', 'Angel Sanz', 'Angel Sigueros', 'Carlos']
alumno_a_calificar = pendientes_calificacion.pop()
print(f"alumno_a_calificar {alumno_a_calificar}")

alumno_a_calificar = pendientes_calificacion.pop()
print(f"alumno_a_calificar {alumno_a_calificar}")

fila_supermercado = ['persona1', 'persona2', 'persona3', 'persona4', 'Alan']
persona_a_atender = fila_supermercado.pop(0)
print(f"persona_a_atender {persona_a_atender}") # persona1

persona_a_atender = fila_supermercado.pop(0)
print(f"persona_a_atender {persona_a_atender}") # persona2

# del() te permite borrar un elemento concreto sin devolverlo (DELETE)
# Ejemplo: productos de un ecommerce, en el checkout antes de finalizar compra eliminamos uno
precios = [5.99, 12.32, 10.00, 48.57]
del precios[2]
# del precios[2]
print(precios)


