"""
Programa para calcular el sesgo de una distribucion de datos aleatoria en funcion de su mediana, media, y moda.
Las condiciones son:

  media > mediana > moda: Sesgo positivo
  media < mediana < moda: Sesgo negativo
  media == mediana == moda: Sin sesgo (Distribucion Simetrica )

Author: Estefi Nelson
Fecha: 12/04/2025
"""

import random
from statistics import mean, median, mode

numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

if media > mediana and mediana > moda:
    print("Distribucion con sesgo positivo (hacia la derecha).")
elif media < mediana and mediana < moda:
    print("Distribucion con sesgo negativo (hacia la izquierda).")
elif media == mediana and mediana == moda:
    print("Distribucion sin sesgo (simetrica).")
else:
    print("No se cumple ninguno de los tres casos (derecha/izquierda/simetrica)")