import time



def verificar_contraseña(contrasena):
    contrasena_ingreso = input("Ingrese su contraseña: ")
    print("\n")
    intentos = 1
    while contrasena != contrasena_ingreso and intentos <= 2:
        print("La contraseña que ingreso no es correcta..")
        time.sleep(intentos)
        contrasena_ingreso = input("Ingrese su contraseña nuevamente: ")
        print("\n")
        intentos += 1

    if contrasena_ingreso == contrasena and intentos <= 3:
        print("¡¡¡Bienvenido!!!")
        print("Fin...")
        return True
    else:
        print("Contraseña bloqueada temporalmente..")
        return False


contrasena = input("Ingrese una contraseña a registrar: ")
print("Contraseña registrada con exito..")
print("\n")

resultado = verificar_contraseña(contrasena)
print(resultado)