"""
Programa que muestra que siguiendo con el diccionario precio_frutas, actualiza los precios 
de las siguientes frutas:
Banana = 1330 
Manzana = 1700
Melón = 2800    
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
