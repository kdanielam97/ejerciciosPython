print("=========================================================================")
print("                            = CALCULADORA =                              ")
print("=========================================================================\n")

print("         ....................................")
print("                    Menu de opciones         ")
print("         ....................................")
print("\n")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
print("5. Division entera")
print("6. Exponente")
print("7. Modulo o resto")
print("\n")
opcion = int(input("Elige un numero del menu para la opcion deseada: "))
numero_uno = None
numero_dos = None
respuesta = None
if opcion == 1:
    print("        ....................................")
    print("                         Suma               ")
    print("        ....................................")
    print("\n")
    numero_uno = int(input("ingrese el primer numero: "))
    numero_dos = int(input("ingrese el segundo numero: "))
    respuesta = numero_uno + numero_dos
    print("El resultado de la suma de ", numero_uno,
          " + ", numero_dos, " = ", respuesta)
elif opcion == 2:
    print("        ....................................")
    print("                         Resta              ")
    print("        ....................................")
    print("\n")
    numero_uno = int(input("ingrese el primer numero: "))
    numero_dos = int(input("ingrese el segundo numero: "))
    respuesta = numero_uno - numero_dos
    print("El resultado de la resta de ", numero_uno,
          " - ", numero_dos, " = ", respuesta)
elif opcion == 3:
    print("       ....................................")
    print("                  multiplicacion           ")
    print("       ....................................")
    print("\n")
    numero_uno = int(input("ingrese el primer numero: "))
    numero_dos = int(input("ingrese el segundo numero: "))
    respuesta = numero_uno * numero_dos
    print("El resultado de la multiplicacion de ",
          numero_uno, " x ", numero_dos, " = ", respuesta)
elif opcion == 4:
    print("       ....................................")
    print("                      Division             ")
    print("       ....................................")
    print("\n")
    numero_uno = int(input("ingrese dividendo: "))
    numero_dos = int(input("ingrese el divisor: "))
    if numero_dos == 0:
        print("no se puede dividir ningún número entre cero (0) porque "
              "el resultado es indeterminado o infinito")
    else:
        respuesta = numero_uno / numero_dos
        respuesta = round(respuesta, 2)
        print("El resultado de la division de ", numero_uno,
              " / ", numero_dos, " = ", respuesta)
elif opcion == 5:
    print("      ....................................")
    print("                  Division entera         ")
    print("      ....................................")
    print("\n")
    numero_uno = int(input("ingrese dividendo: "))
    numero_dos = int(input("ingrese el divisor: "))
    respuesta = numero_uno // numero_dos
    print("El resultado de la division de los numeros enteros ",
          numero_uno, " / ", numero_dos, " = ", respuesta)
elif opcion == 6:
    print("       ....................................")
    print("                      Exponente            ")
    print("       ....................................")
    print("\n")
    numero_uno = float(input("ingrese el numero base: "))
    numero_dos = float(input("ingrese el exponente: "))
    if numero_uno < 0 and numero_dos % 2 == 0:
        print("No se puede calcular la potencia de un número negativo a un exponente fraccionario con un denominador par")
    elif numero_uno < 0 and numero_dos % 2 != 0:
        print("La potencia de un número negativo a un exponente fraccionario con un denominador impar es posible")
    # realizar el cálculo
    elif type(numero_dos) == float and numero_dos % 1 != 0:
        print("No se puede calcular la potencia de un número negativo a un exponente irracional")
    elif pow(numero_uno, numero_dos) == float("inf"):
        print("El resultado es infinito")
    else:
        respuesta = pow(numero_uno, numero_dos)
        if type(respuesta) == float:
            print("Base ", numero_uno, " Exponente ",
                  numero_dos, " = ", respuesta)
        else:
            print("Base ", numero_uno, " Exponente ",
                  numero_dos, " = ", int(respuesta))
elif opcion == 7:
    print("       ....................................")
    print("                   Modulo o resto          ")
    print("       ....................................")
    print("\n")
    numero_uno = int(input("ingrese dividendo: "))
    numero_dos = int(input("ingrese el divisor: "))
    respuesta = numero_uno % numero_dos
    print("EL modulo resultante entre la division de ",
          numero_uno, " / ", numero_dos, " = ", respuesta)

else:
    print("El numero de la opcion que ingresaste no existe, vuelve a intentar")