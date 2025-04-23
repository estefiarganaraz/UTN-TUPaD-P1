"""
Programa que imprime en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente.
"""

n = 100
while n >= 0:
    if n % 2 == 0:
        print(n)
    n -= 1