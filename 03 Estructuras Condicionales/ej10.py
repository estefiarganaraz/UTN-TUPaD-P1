"""
Programa que imprime el periodo del año segun:
Estación en el hemisferio norte
Desde el 21 de diciembre hasta el 20 de marzo:
Invierno
Estación en el hemisferio sur
Verano
Desde el 21 de marzo hasta el 20 de junio
Estación en el hemisferio norte
Primavera 
Estación en el hemisferio sur
Otoño
Desde el 21 de junio hasta el 20 de
septiembre (incluidos)
Estación en el hemisferio norte
Verano
Estación en el hemisferio sur
Invierno
Desde el 21 de septiembre hasta el 20 de
diciembre 
Estación en el hemisferio norte
Otoño 
Estación en el hemisferio sur
Primavera
Author= Estefania Nelson
Date= 12/4/2025
"""

hemisferio = int(input("Ingrese el hemisferio (Norte=1/Sur=2): "))
mes = int(input("Ingrese el mes (Enero=1,Febrero=2,Marzo=3,Abril=4,Mayo=5,Junio=6,Julio=7,Agosto=8,Septiembre=9,Octubre=10,Noviembre=11,Diciembre=12): "))
dia = int(input("Ingrese el dia (del 1 al 31): "))


if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
    if hemisferio == 1:
        print("Invierno")
    else:
        print("Verano")
elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
    if hemisferio == 1:
        print("Primavera")
    else:
        print("Otoño")
elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
    if hemisferio == 1:
        print("Verano")
    else:
        print("Invierno")
elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
    if hemisferio == 1:
        print("Otoño")
    else:
        print("Primavera")


    

