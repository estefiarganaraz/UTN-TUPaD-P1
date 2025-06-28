"""
Crear una lista con los números del 1 al 100 que sean múltiplos de 4.
Utilizar la función range.
"""

multiplos_de_4 = []
for n in range(1, 101, 1):
    if n % 4 == 0:
        multiplos_de_4.append(n)

print(multiplos_de_4)
