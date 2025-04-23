"""
Programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos
números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos.
(Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).
"""

total_numeros = 100

pares = 0
impares = 0
positivos = 0
negativos = 0

cantidad_ingresados = 0
while cantidad_ingresados < total_numeros:

    numero_ingresado = int(input("Ingrese un numero: "))
    cantidad_ingresados += 1

    if numero_ingresado > 0:
        positivos += 1
        if numero_ingresado % 2 == 0:
            pares += 1
        else:
            impares += 1
    elif numero_ingresado < 0:
        negativos += 1
        if numero_ingresado % 2 == 0:
            pares += 1
        else:
            impares += 1
    else:
        pares += 1

print(f"Numeros pares {pares} y numeros impares {impares}")
print(f"Numeros positivos {positivos} y numeros negativos {negativos}")