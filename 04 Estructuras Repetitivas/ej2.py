"""
Programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene.
"""

numero = int(input("Ingrese un numero: "))

cantidad_digitos = 0
while numero >= 10:
    cantidad_digitos += 1
    numero = numero // 10
cantidad_digitos += 1

print(f"El numero tiene {cantidad_digitos} digitos")