"""
Programa que crea una agenda donde las claves sean tuplas de (día, hora)
y los valores sean eventos. Permite consultar qué actividad hay en cierto día y hora
"""

agenda = {
    ("Lunes", "18:00"): "Reunión",
    ("Martes", "15:00"): "Clase de Inglés"
    }

dia = input("Día: ")
hora = input("Hora: (HH:MM): ")

evento = agenda.get((dia, hora), "No hay eventos programados")
print(f"Evento: {evento}")