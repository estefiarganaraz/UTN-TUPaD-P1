"""
Crear dos funciones: calcular_area_circulo(radio) 
que reciba el radio como parámetro y devuelva el área del círculo. 
calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
"""

import math 

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio


radio = float(input("Ingrese el radio del circulo: "))
area = calcular_area_circulo(radio)
print(f"El area del circulo es {area}")
perimetro = calcular_perimetro_circulo(radio)
print(f"El perimetro del circulo es {perimetro}")
