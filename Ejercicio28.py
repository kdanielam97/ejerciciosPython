

valor_uno = float(input("Ingresa el primer valor a comparar: "))
valor_dos = float(input("Ingresa el segundo valor a comparar: "))
print("\n")
if valor_uno > valor_dos:
    print(valor_uno, " es mayor que ", valor_dos)
elif valor_dos > valor_uno:
    print(valor_dos, " es mayor que ", valor_uno)
else:
    print("Los valores ", valor_uno, " y ", valor_dos, " son iguales ")