print("        ************************************************************")
print("                                    SALUDO                          ")
print("        ************************************************************")
print("\n")

nombre = input("Ingresa tu nombre: ")
nom_imprime = nombre
nombre = nombre.lower().split()
if "daniela" in nombre:
    print("Holiii!!!!!")
else:
    print(f"Hola {nom_imprime} ¡bunas noches!")