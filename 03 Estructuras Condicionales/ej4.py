""" 
Programa que categoriza edades.
Author= Estefania Nelson
Date= 6/4/2025
"""

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")
