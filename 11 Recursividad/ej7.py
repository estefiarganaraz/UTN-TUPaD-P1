"""
Programa que escribe una función recursiva contar_bloques(n), que recibe el número de bloques en el
nivel más bajo, y devuelve el total de bloques que necesita para construir toda la pirámide.
Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.
Ejemplos:
contar_bloques(1) → 1
(1)
contar_bloques(2) → 3
(2 + 1)
contar_bloques(4) → 10
(4 + 3 + 2 + 1)
"""


def contar_bloques(n_ultimo_nivel):
    if n_ultimo_nivel == 1:
        return 1
    else:
        return n_ultimo_nivel + contar_bloques(n_ultimo_nivel-1)
    
print("Ingrese numeros que representen la cantidad de bloques en el último nivel de la pirámide.")
print("('exit') para salir.")
ingresando = True
while ingresando:
    entrada = input()
    if entrada == 'exit':
        ingresando = False
    else:
        entrada = int(entrada)
        if entrada > 0:
            print(f"La cantidad de bloques que tiene la pirámide en total es {contar_bloques(entrada)}")
        else:
            print(f"Por favor ingrese números positivos")