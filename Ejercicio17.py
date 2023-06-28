

try:
    numero = int(input("Ingresa numero a acumular: "))
    acumulado = []
    while numero != 0:
        acumulado.append(numero)
        numero = int(input("Ingresa numero a acumular: "))
    
    print(f"de los valores acumulados = {acumulado} el total de la suma es = {sum(acumulado)}")
except:
    print("El valor ingresado no es correcto")