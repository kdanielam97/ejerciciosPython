
numeros = int(input("¿Cuantos valores desea ordenar: "))
cantidad_numeros = []
for i in range(numeros):
    valor = int(input("Ingrese el número {} de {}: ".format(i+1, numeros)))
    cantidad_numeros.append(valor)
    numeros_ordenados = sorted(cantidad_numeros)
print("Los numeros ingresados se organizan de la siguiente manera ", numeros_ordenados)