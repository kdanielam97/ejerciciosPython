

try:
    oracion = input("Ingresa una oracion: ")
    letra = input("¿Que letra de la oracion aterior deseas buscar?: ")
    letras = []
    print(len(oracion))
    for i in range(len(oracion)):
        if oracion[i].lower() == letra:
            letras.append(letra)
    
    print(f"En la oracion {oracion} se encontro {len(letras)} veces la letra {letra} ")
except:
    print("los datos ingresados no son correctos.")