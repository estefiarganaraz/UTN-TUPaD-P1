"""
Programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.
"""

limite_inferior = int(input("Ingrese el primer numero (min): "))
limite_superior = int(input("Ingrese el segundo numero (max): "))


if limite_superior > limite_inferior:
    suma = 0
    for n in range(limite_inferior + 1, limite_superior):
        suma += n

    print(
        f"La suma de los numeros entre {limite_inferior} y {limite_superior} es {suma}"
    )
else:
    print("Ingrese los datos correctamente")