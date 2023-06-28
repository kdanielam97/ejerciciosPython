
def CantidadLista(datoLista):
    numeroLista = ""
    if datoLista < 40:
        numeroLista = len(datoLista)
    elif datoLista >= 40 or datoLista <= 50:
        peso_entre40_50.append(peso)
    elif datoLista > 50 or datoLista < 60:
        peso_entre51_59.append(peso)
    elif peso > 50 or peso < 60:
        peso_mayor_60.append(peso)




alumnos = int(input("Ingresa la cantidad de alumnos a ingresar: "))
peso_menos_40 = []
peso_entre40_50 = []
peso_entre51_59 = []
peso_mayor_60 = []

for i in range(0, alumnos, 1):
    peso = int(input(f"Ingresa el peso en kg del alumno {i+1}: "))
    if peso < 40:
        peso_menos_40.append(peso)
    elif peso >= 40 and peso <= 50:
        peso_entre40_50.append(peso)
    elif peso > 50 and peso < 60:
        peso_entre51_59.append(peso)
    elif peso >= 60:
        peso_mayor_60.append(peso)

print("\n")
print(f"hay {len(peso_menos_40)} alumnos = {peso_menos_40} con un peso de menos de 40kg ")
print(f"hay {len(peso_entre40_50)} alumnos = {peso_entre40_50} con un peso entre 40 y 50 kg ")
print(f"hay {len(peso_entre51_59)} alumnos = {peso_entre51_59} con un peso mayor a 50 y menor a 60 kg ")
print(f"hay {len(peso_mayor_60)} alumnos = {peso_mayor_60} con un peso mayor o igual a 60 kg ")