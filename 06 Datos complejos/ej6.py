"""
Programa que muestra los nombres de 3 alumnos, y para cada uno,
una tupla de 3 notas. Luego, muestra el promedio de cada alumno.
"""

alumnos = {}

print("Ingrese 3 alumnos y sus notas")
for i in range(3):
    nombre = input(f"Nombre del alumno {i+1}")
    notas = (
        float(input("Nota 1: ")),
        float(input("Nota 2: ")),
        float(input("Nota 3: "))
    )
    alumnos[nombre] = notas

print("Promedios")
for nombre, notas in alumnos.items():
    suma = 0
    total = len(notas)
    promedio = suma / total 
    print(f"{nombre}: {promedio}")