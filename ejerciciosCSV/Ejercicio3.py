import csv
with open("jefes_hollow_knight.csv", encoding="utf-8") as archivo:
    reader = csv.DictReader(archivo) # lo leemos como diccionario para coger el valor del item nombre
    for row in reader:
        print(row['nombre'])