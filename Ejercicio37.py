
dividendo = int(input("Ingresa un numero: "))
numero = dividendo
divisor = 2
total_residuo = []
while dividendo >= 1:
    residuo = dividendo % divisor
    total_residuo.insert(0, residuo)
    dividendo = dividendo // divisor
binario = "".join(str(i) for i in total_residuo)
print("El numero decimal ", numero, " en binario es igual a ", binario)