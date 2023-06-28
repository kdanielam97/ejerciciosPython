

entero = None
flotante = None
cadena = None

dato = input("Ingrese un dato en letras o numeros: ")
dato = dato.lower()
print("\n")
if dato.isnumeric():
    entero = int(dato)
    tipo_de_dato = type(entero)
    print("El valor", dato, " es un ", tipo_de_dato.__name__)
elif "." in dato:
    flotante = float(dato)
    tipo_de_dato = type(flotante)
    print("El valor", dato, " es un ", tipo_de_dato.__name__)
elif dato == "verdadero" or dato == "true" or dato == "falso" or dato == "false":
    print("El valor", dato, " es un ", "Bolean")
else:
    cadena = dato
    cadena = type(cadena)
    print("El valor", dato, " es un ", cadena.__name__)