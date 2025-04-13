""" 
Programa que pide ingresar una contraseña de entre 8 y 14 caracteres.
Author= Estefania Nelson
Date= 6/4/2025
"""

password = input("Ingrese su contraseña: ") 

cantidad_caracteres = len(password)

if cantidad_caracteres >= 8 and cantidad_caracteres <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

