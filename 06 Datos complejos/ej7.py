"""
Programa que dado dos sets de números, representando dos listas de estudiantes que 
aprobaron Parcial 1 y Parcial 2:
Muestra los que aprobaron ambos parciales
Muestra los que aprobaron solo uno de los dos
Muestra la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)
"""

parcial_1 = {1,3,5,7,9,12}
parcial_2 = {1.7,9,13,15,18}

ambos = parcial_1.intersection(parcial_2)
print(f"Aprobaron ambos parciales: {ambos}")

solo_uno = parcial_1.symmetric_difference(parcial_2)
print(f"Aprobaron solo un parcial: {solo_uno}")

al_menos_uno = parcial_1.union(parcial_2)
print(f"Aprobaron al menos un parcial: {al_menos_uno}")