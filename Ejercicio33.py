print("========================================")
print("         NUMERO POTENCIA DE DOS         ")
print("========================================")
print("\n")


def es_potencia_de_dos(numero):
    if numero <= 0:
        return False
    return (numero & (numero - 1)) == 0  # operación bitwise AND


def suma_potencias_de_dos(rango_inicio, rango_fin):
    suma = 0
    for num in range(rango_inicio, rango_fin + 1):
        if es_potencia_de_dos(num):
            suma += num
    return suma


print(es_potencia_de_dos(20))
print(suma_potencias_de_dos(1, 20))