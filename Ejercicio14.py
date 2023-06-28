print("        ************************************************************")
print("                    NUMERO DE VOCALES EN UNA ORACION                ")
print("        ************************************************************")
print("\n")

frase = input("Ingresa una frase: ")
a = []
e = []
i = []
o = []
u = []
for j in frase:
    if j.lower() == "a":
        a.append(j)
    elif j.lower() == "e":
        e.append(j)
    elif j.lower() == "i":
        i.append(j)
    elif j.lower() == "o":
        o.append(j)
    elif j.lower() == "u":
        u.append(j)
print(f"En la frase {frase} hay {len(a)} letras a, {len(e)} letras e, {len(i)} letras i, {len(o)} letras o, {len(u)} letras u", end="")