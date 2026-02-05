import csv

palabraBuscar = input("Ingrese el nombre del jefe a buscar: ")

palabraBuscar = palabraBuscar.strip().lower()

promediosMayor5 = []

with open("jefes_hollow_knight.csv", encoding="utf-8") as f:
    lista = []
    #lector = csv.reader(f, delimiter=";") por si tienes otro delimitador
    palabras = csv.DictReader(f)
    encabezados = palabras.fieldnames

    for palabra in palabras:
        nombre_csv = palabra['nombre'].strip().lower()

        if nombre_csv in palabraBuscar:
            lista.append(palabra)

        if float(palabra['promedio_derrotas']) > 5.0:
            promediosMayor5.append(palabra)

    for palabra in lista:
        print(
            f"\nNombre: {palabra['nombre']}"
            f"\nTipo: {palabra['tipo']}"
            f"\nLocalización: {palabra['localizacion']}"
            f"\nPromedio de derrotas: {palabra['promedio_derrotas']}"
            f"\n{'-'*30}" # agrega lineas de separación
        )

with open ("hollow_knightPromedios.csv.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames = encabezados)
    writer.writeheader()
    writer.writerows(promediosMayor5)
