

nombre = input("Ingresa tu nombre: ")
horas_trabajadas = int(
    input(nombre + " Ingresa la cantidad de horas trabajadas: "))
valor_hora = int(input(nombre + " Ingresa el valor de la hora de trabajo: "))

if horas_trabajadas <= 35:
    horas_mayor_35 = 0
    horas_menor_35 = horas_trabajadas
    total_menor_35 = valor_hora * horas_trabajadas
    total_a_pagar = total_menor_35
elif horas_trabajadas > 35:
    horas_menor_35 = 35
    horas_mayor_35 = horas_trabajadas - 35
    valor_hora_exedente = valor_hora * 1.5
    total_mayor_35 = valor_hora_exedente * horas_mayor_35
    total_menor_35 = valor_hora * 35
    total_a_pagar = total_menor_35 + total_mayor_35

if total_a_pagar > 2000000 and total_a_pagar < 2220000:
    impuesto = (total_a_pagar - 2000000) * (20/100)
elif total_a_pagar > 2220001:
    impuesto_20 = 220000 * (20/100)
    impuesto = (total_a_pagar - 2220000) * (30/100)
    impuesto = impuesto_20 + impuesto
else:
    impuesto = 0

total_neto = total_a_pagar - impuesto
print("\n")
print("------------------------ {} ------------------------".format(nombre))
print("HORAS-N  HORAS-E  VALOR HORA      TOTAL/H         IMPUESTO        NETO A PAGAR")
print("{:^8} {:^8} ${:^10.2f} ${:^14.2f} ${:^14.2f} ${:^20.2f}".format(
      horas_menor_35, horas_mayor_35, valor_hora, total_a_pagar, impuesto, total_neto))