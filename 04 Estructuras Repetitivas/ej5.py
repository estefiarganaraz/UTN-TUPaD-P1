"""
Programa que crea un juego en el que el usuario debe adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
"""

import random

numero_secreto = random.randint(0, 9)
cantidad_intentos = 0
numero_ingresado = 9999
while numero_ingresado != numero_secreto:
    numero_ingresado = int(input("Ingrese un numero entero entre 0 y 9: "))
    cantidad_intentos += 1

print(f"Ok, el numero secreto era {numero_secreto}. Necesitaste {cantidad_intentos} intentos")