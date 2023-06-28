print("---------------------------------------------------------")
print("----------OPERACIONES CON NUMEROS FRACCIONARIOS----------")
print("---------------------------------------------------------")
# FUNCION PARA DETERMINAR SI UN NUMERO ES PRIMO O NO
def n_primo(numero):
    if numero <= 1:
        return False
    else:
        for div in range(2, int(numero+1), +1):
            if numero % div == 0:
                return False
        return True  # si es primo
# FUNCION PARA DESCOMPONER UN NUMERO EN FACTORES PRIMOS
def descomponer_factores_primos(valor):
    contador = 2
    lista = []
    while valor != 1:
        if valor % contador == 0:
            valor //= contador
            lista.append(contador)
        else:
            contador += 1  # Incrementa el contador si no es un factor primo
    return lista

"""def multiplicar(lista):
    resultado = 1
    for i in lista:
        resultado *= i
    return resultado"""
# FUNCION PARA CALCULAR MINIMO COMUN MULTIPLO
def calcular_mcm(n1, n2):
    # FUNCION PARA CALCULAR MAXIMO COMUN DIVISOR
    def calcular_mcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x
    mcd = calcular_mcd(abs(n1), abs(n2))
    mcm = abs(n1 * n2) // mcd
    return mcm
# FUNCION PARA CALCULAR MINIMO COMUN MULTIPLO PARA MAS DE DOS VALORES 
def calcular_varios_mcm(valores):
    mcm_resultado = valores[0]
    for i in range(1, len(valores)):
        mcm_resultado = calcular_mcm(mcm_resultado, valores[i])
    return mcm_resultado

a = abs(int(input("Ingresa el numerador a: ")))
b = int(input("Ingresa el denominador b: "))
c = abs(int(input("Ingresa el numerador c: ")))
d = int(input("Ingresa el denominador d: "))
e = abs(int(input("Ingresa el numerador e: ")))
f = int(input("Ingresa el denominador f: "))

if b == 0 or d == 0 or f == 0:
    print("El denominador debe ser diferente a cero.")
else:
    # SE CREAN VARIABLES G,H,I PARA OBTENER FACTORES PRIMOS 
    print("---------------------------------------------------------")
    print("----------------------FACTORES PRIMOS--------------------")
    print("---------------------------------------------------------")
    g = descomponer_factores_primos(abs(b))
    h = descomponer_factores_primos(abs(d))
    i = descomponer_factores_primos(abs(f))

    print(g, h, i)
    # SE CREA UNA LISTA PARA GUARDAR LOS VALORES DE LOS CUALES SE DESEA OBTENER EL MCM
    print("---------------------------------------------------------")
    print("-------------------MINIMO COMUN MULTIPLO-----------------")
    print("---------------------------------------------------------")
    valores_mcm = [b, d, f]
    factor = calcular_varios_mcm(valores_mcm)
    print(factor)
    print("---------------------------------------------------------------------")
    print("---SE MULTIPLICA ESTOS VALORES CON LOS NUMERADORES Y DENOMINADORES---")
    print("---------------------------------------------------------------------")
    b = factor // b
    d = factor // d
    f = factor // f
    print(b, d, f)
    a = a * b
    c = c * d
    e = e * f
    print("---------------------------------------------------------")
    print("-------------------------RESULTADOS----------------------")
    print("---------------------------------------------------------")
    print(f"Numeradores = {a}, {c}, {e}")
    print(f"Denominador = {factor}")
    numeradores = a + c - e

    print(f"Resultado = {numeradores} / {factor}")

    s = 2
    while numeradores % s == 0:
        numeradores //= s
        factor //= s
        s += 1
    print(f"Resultado simplificado = {numeradores} / {factor}")