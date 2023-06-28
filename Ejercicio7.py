print("==========")
print("CONVERSOR")
print("==========\n")
print("Menu de opciones: \n")

print("preciona 1 si deseas convertir de numero a palabra")
print("preciona 2 si deseas convertir de palabra a numero\n")
opcion_seleccionada = int(input("¿Cual es la opcion deseada? "))

if opcion_seleccionada == 1:
    print("\nConversor de numero a palabra.\n")
    numero = int(input("escribe le numero que deseas convertir a palabra: "))
    if numero == 1:
        print("El numero ingresado es 'UNO'")
    elif numero == 2:
        print("El numero ingresado es 'DOS'")
    elif numero == 3:
        print("El numero ingresado es 'TRES'")
    elif numero == 4:
        print("El numero ingresado es 'CUATRO'")
    elif numero == 5:
        print("El numero ingresado es 'CINCO'")
    else:
        print("El programa solo puede convertir hasta el numero 5.")
elif opcion_seleccionada == 2:
    print("Conversor de palabra a numero.\n")
    palabra = input("Ingresa la palabra que deseas convertir a numero: ")
    palabra = palabra.lower()
    if palabra == "uno":
        print("la palabra ingresada es '1'")
    elif palabra == "dos":
        print("la palabra ingresada es '2'")
    elif palabra == "tres":
        print("la palabra ingresada es '3'")
    elif palabra == "cuatro":
        print("la palabra ingresada es '4'")
    elif palabra == "cinco":
        print("la palabra ingresada es '5'")
    else:
        print("la palabra ingresada no es posible convertirla a numero")
else:
    print("Opcion no didponible.")
print("¡¡¡FIN!!!")