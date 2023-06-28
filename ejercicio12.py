placa = (input("ingrese la placa: "))
semana = ["lunes", "martes", "miercoles", "jueves", "viernes"]
            #0        #1        #3           #4        #5

try:
    x= int(placa[5])
except:
    x= int(placa[4])

if x == 1 or x == 2:
    print ("tu dia de pico y placa es", semana[4])
elif x == 3 or x == 4:
    print ("tu dia de pico y placa es ", semana[0]) 
elif x == 5 or x == 6:
    print("tu dia de pico y placa es ", semana[1]) 
elif x == 7 or x == 8:
    print("tu dia de pico y placa es ", semana[2]) 
elif x == 9 or x == 0:
    print("tu dia de pico y placa es ", semana[3])
else:
    print("ingrese un valor valido")                      