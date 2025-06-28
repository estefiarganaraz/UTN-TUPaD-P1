"""
Programa que crea una función recursiva, que calcula el factorial de un número. 
Luego, utiliza esa función para calcular y mostrar el factorial de todos los números enteros
entre 1 y el número que indique el usuario.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n




numero_ingresado = int(input("Ingrese un límite superior: "))
for n in range(1, numero_ingresado + 1):
    print(f"El factorial de {n} es {factorial(n)}")