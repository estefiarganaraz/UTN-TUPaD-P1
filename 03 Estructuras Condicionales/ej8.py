"""
Programa que solicita al usuario el ingreso de su nombre, y una opcion. 
Si la opcion es 1, muestra su nombre en mayusculas.
Si la opcion es 2, muestra su nombre en minusculas.
Si la opcion es 3, muestra su nombre capitalizado.
En otro caso, muestra "Opcion incorrecta".
Author= Estefania Nelson
Date= 11/4/2025
"""

nombre = input("Ingrese su nombre: ")

opcion = int(input("Ingrese una opcion (1=Mayusculas 2=Minusculas, 3=Capitalizado): "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opcion incorrecta")
