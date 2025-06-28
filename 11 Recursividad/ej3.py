"""
Programa que crea una función recursiva, que calcula la potencia de un número base elevado a un
exponente, utilizando la fórmula nm = n ∗ n(m−1). Prueba esta función en un
algoritmo general.
"""

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente -1)


for base in range(1, 5 + 1):
    for exponente in range(0, 5 + 1):
        print(f"{base} elevado a la {exponente} es {potencia(base, exponente)}")
