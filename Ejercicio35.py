print("        ************************************************************")
print("                DECIMAL A BINARIO, HEXADECIMAL Y OCTAL              ")
print("        ************************************************************")
print("\n")

print("========================================")
print("            Menu de opciones            ")
print("========================================")
print("\n")
print("1. Convertir decimal a binario")
print("2. Convertir decimal a hexadecimal")
print("3. Convertir decimal a octal")
print("\n")
try:
    opcion = int(input("Coloca el numero de la opcion elegida: "))

    if opcion > 0 or opcion < 4:
        if opcion == 1:
            print("========================================")
            print("       Convertir decimal a binario      ")
            print("========================================")
            print("\n")
            try:
                numero = int(input("Ingresa un numero: "))
                num_imprime = numero
                base = 2
                lista_binario = []
                while numero > 0:
                    if numero % base == 0:
                        lista_binario.append(0)
                    else:
                        lista_binario.append(1)
                    numero = numero // base
                lista_binario.reverse()
                lista_binario = str(lista_binario).replace(
                    "[", "").replace("]", "").replace(",", "")
                print("El numero ", num_imprime,
                      " en binario es igual a ", lista_binario)
            except ValueError:
                print("Debes ingresar un número entero.")

        elif opcion == 2:
            print("========================================")
            print("     Convertir decimal a hexadecimal    ")
            print("========================================")
            print("\n")
            try:
                numero = int(input("Ingresa un numero: "))
                num_imprime = numero
                base = 16
                lista_hexadecimal = []
                while numero >= base:
                    modulo = numero % base
                    if modulo == 10:
                        lista_hexadecimal.append("A")
                    elif modulo == 11:
                        lista_hexadecimal.append("B")
                    elif modulo == 12:
                        lista_hexadecimal.append("C")
                    elif modulo == 13:
                        lista_hexadecimal.append("D")
                    elif modulo == 14:
                        lista_hexadecimal.append("E")
                    elif modulo == 15:
                        lista_hexadecimal.append("F")
                    else:
                        lista_hexadecimal.append(str(modulo))
                    numero = numero // base
                ultimo_modulo = numero % base
                lista_hexadecimal.append(str(ultimo_modulo))
                lista_hexadecimal.reverse()
                resultado = " ".join(lista_hexadecimal)
                print("El numero ", num_imprime,
                      "En hexadecimal es igual a ", resultado)
            except ValueError:
                print("Debes ingresar un número entero.")
        elif opcion == 3:
            print("========================================")
            print("         Convertir decimal a octal      ")
            print("========================================")
            print("\n")
            numero = None
            try:
                numero = int(input("Ingresa un numero: "))
                num_imprime = numero
                base = 8
                lista_octal = []
                while numero >= base:
                    modulo = numero % base
                    lista_octal.append(str(modulo))
                    numero = numero // base
                ultimo_modulo = numero % base
                lista_octal.append(str(ultimo_modulo))
                lista_octal.reverse()
                resultado = " ".join(lista_octal)
                print("El unmero ", num_imprime,
                      "En octal es igual a ", resultado)
            except ValueError:
                print("Debes ingresar un número Entero.")
        else:
            print("Debes ingresar un valor valido")
except ValueError:
    print("Elige una opcion valida 1,2 o 3")