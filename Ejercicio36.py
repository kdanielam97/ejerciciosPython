

numero = input("Ingresa un numero binario: ")
numero_lista = [int(l)for l in numero]
base = 2
resultado = 0

for i in range(0,len(numero_lista),1):
    resultado += numero_lista[i] * (base ** (len(numero_lista) - i - 1))
print(resultado)

i = 0
while i < len(numero_lista):
    resultado += numero_lista[i] * (base ** (len(numero_lista) - i - 1))
    i += 1
print(resultado)