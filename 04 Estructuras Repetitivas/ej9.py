"""
Programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores.
(Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).
"""

cant_numeros = 100

suma = 0
for i in range(cant_numeros):
    numero = int(input("Ingrese el numero: "))
    suma += numero

media = suma / cant_numeros

print(f"La media de los valores {cant_numeros} es {media}")