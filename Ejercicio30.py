try:
    valor = int(input("Ingresa un numero: "))
    i = 0
    vr = 0
    while vr <= valor:
        vr = 2 ** i
        if vr <= valor:
            print(vr, end=" ")
        i += 1
except:
    print("Dato ingresado no es valido")