


def numeroCentral(valor_uno, valor_dos, valor_tres):
    if valor_uno <= valor_dos <= valor_tres or valor_tres <= valor_dos <= valor_uno:
        print(f"{valor_dos} es el numero medio")
    elif valor_dos <= valor_uno <= valor_tres or valor_tres <= valor_uno <= valor_dos:
        print(f"{valor_uno} es el numero medio")
    elif valor_uno <= valor_tres <= valor_dos or valor_dos <= valor_tres <= valor_uno:
        print(f"{valor_tres} es el numero medio")

lista_valor = []
for i in range(1, 4, 1):
    valor = int(input(f"Ingresa el valor {i} "))
    lista_valor.append(valor)

numeroCentral(lista_valor[0], lista_valor[1], lista_valor[2])