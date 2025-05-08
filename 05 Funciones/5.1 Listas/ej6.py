"""
Crear una lista con números del 10 al 30 (incluído),
haciendo saltos de 5 en 5 y mostrar por
pantalla los dos primeros.
"""

numeros = []
for n in range(10, 31, 5):
    numeros.append(n)

print(numeros)
print(numeros[0:2])
