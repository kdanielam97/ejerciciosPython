


print("Introcuce dos numeros a comparar.\n")
valor_uno = int(input("Ingresa el primer valor a comparar: "))
valor_dos = int(input("Ingresa el segundo valor a comparar: "))
print("\n los numeros a comparar son ", valor_uno, " y ", valor_dos, "\n")
if valor_uno != valor_dos:
    print("Es diferente....")
if valor_uno > valor_dos:
    print("Es mayor a....")
if valor_uno < valor_dos:
    print("Es menor a....")
if valor_uno >= valor_dos:
    print("Es mayor o igual a....")
if valor_uno <= valor_dos:
    print("Es menor o igual a....")
if valor_uno == valor_dos:
    print("Los valores son iguales")