"""
Programa que muestra un Sistema de Gestión de Estudiantes con Árbol Binario de Búsqueda (ABB), 
simula el registro, búsqueda y eliminación de IDs de estudiantes
utilizando una estructura de datos ABB, demostrando su eficiencia en operaciones 
de inserción, búsqueda y eliminación.
Programa que muestra un Sistema de Gestión de Estudiantes con Árbol Binario de Búsqueda (ABB)

Simula el registro, búsqueda y eliminación de IDs de estudiantes.

Autores:
Mercado, Marcos Agustín.
Mercado, Marcos Agustín
Nelson, Estefanía
Fecha: 27/06/2025

"""

# 1. Definición del Nodo
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# 2. Estructura del Árbol Binario de Búsqueda (BST)
class BST:
    def __init__(self):
        self.root = None

class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class BST:
    def insert(self, root, key):
        if root is None:
            return Node(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        elif key > root.val:
            root.right = self.insert(root.right, key)
        # Si es igual no se inserta (para evitar duplicados)
        return root

    def search(self, root, key):
        if root is None or root.val == key:
            return root
        elif key < root.val:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete_node(self, root, key):
        if root is None:
            return root
        if key < root.val:
            root.left = self.delete_node(root.left, key)
        elif key > root.val:
            root.right = self.delete_node(root.right, key)
        else:
            # Caso 1: sin hijos o un solo hijo
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # Caso 2: dos hijos -> buscar sucesor
            temp = self.find_min(root.right)
            root.val = temp.val
            root.right = self.delete_node(root.right, temp.val)
        return root

    def in_order_traversal(self, root):
        if root:
            self.in_order_traversal(root.left)
            print(root.val, end=" ")
            self.in_order_traversal(root.right)


# Simulación: Gestión de Estudiantes

campus = BST()

# Inserción de IDs de estudiantes
ids = [1034, 1021, 1099, 1005, 1060]
root = None
for student_id in ids:
    root = campus.insert(root, student_id)
# 4. Código de Prueba (Driver Code)
tree = BST()
root = tree.insert(None, 10)
root = tree.insert(root, 5)
root = tree.insert(root, 15)
root = tree.insert(root, 3)
root = tree.insert(root, 7)

print("IDs registrados (en orden):")
campus.in_order_traversal(root)
print("In-order traversal: ", end="")
tree.in_order_traversal(root)
print()

# Búsqueda de un ID existente y uno no existente
search_ids = [1060, 1100]
for sid in search_ids:
    result = campus.search(root, sid)
    if result:
        print(f"ID {sid} encontrado en el sistema.")
    else:
        print(f"ID {sid} NO encontrado.")

# Eliminación de un ID (simula baja del sistema)
id_to_delete = 1021
print(f"\nEliminando ID {id_to_delete}...")
root = campus.delete_node(root, id_to_delete)

print("IDs actualizados luego de la baja:")
campus.in_order_traversal(root)
root = tree.delete_node(root, 5)
print("In-order traversal after deletion: ", end="")
tree.in_order_traversal(root)
print()