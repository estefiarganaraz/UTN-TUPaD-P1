"""
Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de sumarlos, 
restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
"""

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a // b
    return (suma, resta, multiplicacion, division)

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

resultados = operaciones_basicas(a, b)

print(f"Suma: {resultados[0]}, Resta: {resultados[1]}")
print(f"Multiplicacion: {resultados[2]}, Division: {resultados[3]}")