""" 
Programa que imprime por pantalla si un numero es par o no. 
Author= Estefania Nelson
Date= 6/4/2025
"""

numero = int(input("Ingrese un numero: "))

resto = numero % 2 

if resto == 0:
    print("El numero ingresado es par")
else:
    print("Por favor, ingrese un numero par")