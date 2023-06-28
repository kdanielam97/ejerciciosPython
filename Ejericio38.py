print("========================================")
print("       NUMEROS PARES DE 0 A 200         ")
print("========================================")
print("\n")

pares = []
inpares =[]
for numero in range(201):
    if numero % 2 == 0:
        pares.append(numero)
    

print(f"Numeros pares = {pares}")
