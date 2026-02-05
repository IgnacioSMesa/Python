import csv

busqueda = input("Ingrese el nombre del jefe a buscar: ").strip().lower()

coincidencias = []
promedios_mayor_5 = []

with open("jefes_hollow_knight.csv", encoding="utf-8") as f:
    lector = csv.DictReader(f)
    encabezados = lector.fieldnames

    for fila in lector:
        nombre = fila["nombre"].strip().lower()
        promedio = float(fila["promedio_derrotas"])

        if busqueda in nombre:
            coincidencias.append(fila)

        if promedio > 5:
            promedios_mayor_5.append(fila)

for jefe in coincidencias:
    print(
        f"\nNombre: {jefe['nombre']}"
        f"\nTipo: {jefe['tipo']}"
        f"\nLocalización: {jefe['localizacion']}"
        f"\nPromedio de derrotas: {jefe['promedio_derrotas']}"
        f"\n{'-'*30}"
    )

with open("hollow_knightPromedios.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=encabezados)
    writer.writeheader()
    writer.writerows(promedios_mayor_5)
