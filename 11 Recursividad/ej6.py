"""
Programa que escribe una función recursiva en Python llamada suma_digitos(n), que recibe un
número entero positivo y devuelve la suma de todos sus dígitos.
Restricciones:
No se puede convertir el número a string.
Usar operaciones matemáticas (%, //) y recursión.
Ejemplos:
suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
suma_digitos(9) → 9
suma_digitos(305) → 8 (3 + 0 + 5)
"""

def suma_digitos(numero):
    if numero < 10:
        return numero 
    else:
        return suma_digitos(numero // 10) + (numero % 10)
    
print("Ingrese los números que desea probar de a uno por vez. ('exit') para salir.")
ingresando = True 
while ingresando: 
    entrada = input()
    if entrada == 'exit':
        ingresando = False 
    else: 
        entrada = int(entrada)
        print(f"La suma de los digitos de {entrada} es {suma_digitos(entrada)}")