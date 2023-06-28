import math


valor_radio = float(input("Ingresa el valor del radio del circulo: "))

area = math.pi * valor_radio ** 2
print("\n")
print("El area del circulo que tiene como radio ",
      valor_radio, " es igual a ", round(area, 1))