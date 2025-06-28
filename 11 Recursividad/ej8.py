"""
Programa que escribe una función recursiva llamada contar_digito(numero, digito), que recibe un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelve cuántas veces
aparece ese dígito dentro del número.
Ejemplos:
contar_digito(12233421, 2) → 3
contar_digito(5555, 5) → 4
contar_digito(123456, 7) → 0
"""

def contar_digitos(numero, digito):
    if numero < 10:
        if numero == digito: 
            return 1
        else:
            return 0
    else:
        if numero % 10 == digito:
            return 1 + contar_digitos(numero // 10, digito)
        else:
            return 0 + contar_digitos(numero // 10, digito)
        


casos_prueba = [(7, 3), (7, 7), (12, 1), (12, 2), (12, 4),
    (345, 4), (345, 9), (104, 0), (1221, 2),(13331, 3)]
for (numero, digito) in casos_prueba:
    print(f"La cantidad de veces que aparece {digito} en {numero} es {contar_digitos(numero, digito)}") 
