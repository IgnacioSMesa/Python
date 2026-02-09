import csv

promedio = []
with open("jefes_hollow_knight.csv", encoding="utf-8") as archivo:
    reader = csv.DictReader(archivo)

    for row in reader:
        promedio.append(float(row['promedio_derrotas']))

print(f"Promedio de derrotas: {sum(promedio) / len(promedio)}")