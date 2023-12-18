
# Ejemplo 2: lo mismo pero con un maximo de 3 reintentos

password = "admin"
password_user = ""
intento = 1  # contador para el numero de intentos
max_intentos = 3

while intento <= 3:
    password_user = input("Introduce tu contraseña:")
    if password_user == password:
        print("Credenciales correctas.")
        # ... Invocar una funcion que realice la accion deseada ....
        break  # sale del bucle
    intento += 1

if intento > max_intentos:
    print("Alcanzado limite maximo de intentos(3)")

    print("fin")
