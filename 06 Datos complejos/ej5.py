"""
Programa que solicita al usuario una frase e imprime:
Las palabras únicas (usando un set)
Un diccionario con la cantidad de veces que aparece cada palabra
"""

frase = input("Ingrese una frase")
palabras = frase.split()

palabras_unicas = set(palabras)

recuento = {}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1 

print(f"Palabras únicas: {palabras_unicas}")
print(f"Recuento: {recuento}")