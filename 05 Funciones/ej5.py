"""
Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes.
Solicitar al usuario los segundos y mostrar el resultado usando esta función.
"""

SEGUNDOS_POR_HORA = 3600


def segundos_a_horas(segundos):
    horas = segundos / SEGUNDOS_POR_HORA
    return horas


segundos = int(input("Ingrese la cantidad de segundos: "))
resultado = segundos_a_horas(segundos)
print(f"{segundos} segundos equivalen a {resultado} horas")
