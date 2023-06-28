print("========================================")
print("             SUMA DIVISORES             ")
print("========================================")
print("\n")


def suma_divisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    print(divisores)
    return sum(divisores)


print(suma_divisores(12))