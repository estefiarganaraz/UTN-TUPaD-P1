"""
Programa que crea una función recursiva, que calcula el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique.
"""

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


posicion_max = int(input("Ingrese la posición hasta la cual desea ver la serie de Fibonacci: "))
for pos in range(0, posicion_max):
    print(f"{fibonacci(pos)}", end=", ")
print(f"{fibonacci(posicion_max)}")