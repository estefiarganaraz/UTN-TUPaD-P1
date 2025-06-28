"""
Programa que crea una lista que contiene únicamente las frutas sin los precios
"""

precio_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precio_frutas['Naranja'] = 1200
precio_frutas['Manzana'] = 1500
precio_frutas['Pera'] = 2300

print("Diccionario con nuevas frutas")
print(f"{precio_frutas}")

precio_frutas['Banana'] = 1330
precio_frutas['Manzana'] = 1700
precio_frutas['Melón'] = 2800

print("Diccionario con precios actualizados")
print(f"{precio_frutas}")

lista_frutas = []
for fruta in precio_frutas.keys():
    lista_frutas.append(fruta)

print("Lista de frutas sin precios")
print(f"{lista_frutas}")