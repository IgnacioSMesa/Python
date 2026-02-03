import csv

with open("hollow_knight.csv", encoding="utf-8") as archivo:
    reader = csv.reader(archivo)
    encabezado = next(reader) # para no contar el encabezado
    totalFilas = sum(1 for fila in reader)

print(totalFilas)
