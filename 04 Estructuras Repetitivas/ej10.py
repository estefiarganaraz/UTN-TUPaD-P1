"""
Programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
"""

numero = int(input("Ingrese un numero: "))

invertido = 0
while numero >= 10:
    digito = numero % 10
    invertido = (invertido * 10) + digito
    numero = numero // 10
invertido = (invertido * 10) + numero

print(f"El numero invertido es {invertido}")