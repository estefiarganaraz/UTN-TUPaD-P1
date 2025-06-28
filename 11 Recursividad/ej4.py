"""
Programa que crea una función recursiva en Python, que recibe un número entero positivo en base
decimal, y devuelve su representación en binario como una cadena de texto.
Ejemplo:
Convertir el número 10 a binario:
10 ÷ 2 = 5 resto: 0
5 ÷ 2 = 2 resto: 1
2 ÷ 2 = 1 resto: 0
1 ÷ 2 = 0 resto: 1
Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010".
"""

def decimal_a_binario(decimal):
    if decimal < 2:
        return str(decimal)
    else:
        return decimal_a_binario(decimal//2) + str(decimal % 2)



print("Ingrese números que quiera convertir a binario. ('exit') para salir")
ingresando = True 
while ingresando:
    entrada = input()
    if entrada == 'exit':
        ingresando = False 
    else:
        numero = int(entrada) 
        print(f"El número {numero} convertido a binario es {decimal_a_binario(numero)}")

