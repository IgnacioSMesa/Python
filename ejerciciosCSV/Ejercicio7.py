import csv

productos = [
    {"nombre": "Cuaderno", "precio": 2.49, "cantidad": 200},
    {"nombre": "Regla", "precio": 1.29, "cantidad": 150},
    {"nombre": "Tijeras", "precio": 5.75, "cantidad": 75},
    {"nombre": "Pegamento", "precio": 3.50, "cantidad": 120},
    {"nombre": "Marcador", "precio": 1.99, "cantidad": 300}
]

with open ("inventario.csv", "a", newline='') as file:
    filewriter = csv.writer(file)
    filewriter.writerows(productos)
