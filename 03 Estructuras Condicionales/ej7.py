"""
Programa que solicite una frase al usuario. 
Si el string ingresado termina con vocal, añadir un signo de exclamación al final e
imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla
Author= Estefania Nelson
Date= 12/4/2025
"""

texto = input("Ingresa una frase o palabra: ")

ultima_letra = texto[-1]

if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u":
    print(f"{texto}!")
else:
    print(texto)
