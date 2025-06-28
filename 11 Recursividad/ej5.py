"""
Programa que implementa una función recursiva llamada es_palindromo(palabra), que recibe una
cadena de texto sin espacios ni tildes, y devuelve True si es un palíndromo o False si no lo es.
Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed().
"""

def _es_palindromo(palabra, i, f):

    if i == f:
        return True

    if palabra[i] != palabra[f]:
        return False 
    

    return _es_palindromo(palabra, i+1, f-1)

def es_palindromo(palabra):
    return _es_palindromo(palabra,0,len(palabra)-1)





print("Ingrese palabras para verificar si un Palíndromo. ('exit') para salir.")

palabra = str()
ingresando = True 
while ingresando: 
    palabra = input()
    if palabra == 'exit':
        ingresando = False 
    else:
        print(f"{palabra} es Palíndromo? {es_palindromo(palabra)}") 