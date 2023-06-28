

numero_uno = int(input("Ingresa el numero uno: "))
numero_dos = int(input("Ingresa el numero dos: "))

for i in range(numero_uno, numero_dos+1, 1):
    if i % 2 == 0:
        print(i, end=" ")

