import csv

palabraBuscar = input("Ingrese el nombre del jefe a buscar\nHollow Knight\nHornet\nZote el Poderoso: ")

palabraBuscar = palabraBuscar.strip().lower()

with open("jefes_hollow_knight.csv", encoding="utf-8") as f:
    lista = []
    palabras = csv.DictReader(f)

    for palabra in palabras:
        nombre_csv = palabra['nombre'].strip().lower()

        if nombre_csv in palabraBuscar:
            lista.append(palabra)

    for palabra in lista:
        print(
            f"\nNombre: {palabra['nombre']}"
            f"\nTipo: {palabra['tipo']}"
            f"\nLocalización: {palabra['localizacion']}"
            f"\nPromedio de derrotas: {palabra['promedio_derrotas']}"
            f"\n{'-'*30}" # agrega lineas de separación
        )
