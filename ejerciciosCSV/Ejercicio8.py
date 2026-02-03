import csv

datos = [
    {"Nombre": "Natalia", "Edad": "20", "Grado": "A" },
    {"Nombre": "Fran", "Edad": "19", "Grado": "B"},
    {"Nombre": "Nacho", "Edad": "21", "Grado": "C"},
]

fieldnames = ["Nombre", "Edad", "Grado"]
with open("estudiantes.csv", "a", newline='') as file:
    writewriter = csv.DictWriter(file, fieldnames=fieldnames)
    writewriter.writerows(datos)

