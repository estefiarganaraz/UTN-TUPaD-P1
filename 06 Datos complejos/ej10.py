"""
Programa que muestra un diccionario que mapea nombres de países con sus capitales,
y construye un nuevo diccionario dónde:
Las capitales sean las claves
Los países sean los valores
"""

original = {"Argentina": "Buenos Aires", "Brasil": "Brasilia", "Santiago": "Chile"}
invertido = {}

for pais, capital in original.items():
    invertido[capital] = pais 

print(f"{invertido}")