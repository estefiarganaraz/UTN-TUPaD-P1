"""
Programa que muestra almacenes y consultas de números telefónicos.
Permite al usuario cargar 5 contactos con su nombre como clave y número como valor. 
Luego, pide un nombre y muestra el número asociado, si existe.
"""

contactos = {}

print("Carga 5 contactos")
for i in range(5):
        nombre = input(f"Nombre {i+1}: ")
        telefono = input(f"Teléfono de {nombre}: ")
        contactos[nombre] = telefono 

nombre_buscar = input("Buscar teléfono de: ")
if nombre_buscar in contactos: 
    print(f"Teléfono: {contactos[nombre_buscar]}")
else:
    print("Contacto no encontrado")