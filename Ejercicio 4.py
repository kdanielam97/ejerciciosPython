
try:
    anio = int(input("Ingresa un año: "))

    if anio % 4 == 0:
        print(f"El año {anio} es bisiesto")
    else:
        print(f"El año {anio} no es bisiesto")
except:
    print("Dato ingresado no es valido")