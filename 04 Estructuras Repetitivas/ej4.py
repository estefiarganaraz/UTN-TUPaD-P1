"""
Programa que permita al usuario ingresar números enteros y los sume en
secuencia. 
El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.
"""

total = 0
continuar = True

while continuar:
    num = int(input("Ingrese un numero: "))
    
    if num == 0:
        continuar = False 
    else:
        total += num 

print(f"El total acumulado es {total}")