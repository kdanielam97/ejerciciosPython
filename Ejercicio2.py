"""Elaborar un programa  que  convierta  un  numero decimal ingresado  por teclado a
numero  binario, al final  deberá mostrar cual es su equivalencia"""

decimal= int (input("ingresa un numero decimal: "))

if decimal == 0 :
    print("el numero binario equivalente es: 0")
else :
   binario = ""
while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario
        decimal = decimal // 2

print("El número binario equivalente es:", binario)     

