

valor_uno = float(input("Ingrese el primer valor: "))
valor_dos = float(input("Ingrese el segundo valor: "))
valor_tres = float(input("Ingrese el tercer valor: "))

valor_mayor = max(valor_uno, valor_dos, valor_tres)
print("El valor numero es ", valor_mayor)
if valor_uno < valor_dos < valor_tres:
    print(f"El numero mayor es: {valor_tres}")

if valor_uno > valor_dos > valor_tres:
    print(f"El numero mayor es: {valor_uno}")

if valor_dos > valor_uno > valor_tres:
    print(f"El numero mayor es: {valor_dos}")

if valor_uno > valor_dos:
    if valor_uno > valor_tres:
        print(f"El numero mayor es: {valor_uno}")
if valor_dos > valor_uno:
    if valor_dos > valor_tres:
        print(f"El numero mayor es: {valor_dos}")
if valor_tres > valor_uno:
    if valor_tres > valor_dos:
        print(f"El numero mayor es: {valor_tres}")