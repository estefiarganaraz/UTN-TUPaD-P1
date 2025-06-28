"""
Programa que muestra un diccionario donde las claves sean nombres de productos 
y los valores su stock. Permite al usuario:
Consultar el stock de un nuevo producto ingresado
Agregar unidades al stock si el producto ya existe
Agregar un nuevo producto si no existe
"""

inventario = {'Sal': 50, 'Leche': 30, 'Pan': 20}
opcion = ""

while opcion != "3":
    print ("N1.Consultar stock/N2.Modificar stock/N3.Salir")
    opcion = input("Opción: ")

if opcion == "1":
    producto = input("Producto: ")
    print(f"Stock: {inventario.get(producto, 'No existe')}")

elif opcion == "2":
    producto = input("Producto: ")
    cantidad = int(input("Cantidad: "))
    inventario[producto] = inventario.get(producto, 0) + cantidad
    print(f"Nuevo stock de {producto}: {inventario[producto]}")