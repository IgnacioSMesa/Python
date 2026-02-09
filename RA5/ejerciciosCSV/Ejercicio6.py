import csv

with open ("empleados.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if float(row["Salario"]) > 3000: print(row)