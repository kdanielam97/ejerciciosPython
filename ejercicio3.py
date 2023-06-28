binario = input("Ingresa un número binario: ")
decimal = 0
posicion = len(binario) - 1

for digito in binario:
    if digito == '1':
        decimal += 2 ** posicion
    posicion -= 1

print("El número decimal equivalente es:", decimal)