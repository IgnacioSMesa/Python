import csv

producto = input("Ingrese producto a eliminar:")

productoNormalizado =producto.lower().replace(" ","")

filas_filtradas = []

with open("inventario.csv", encoding="utf-8") as file:
    contenido = csv.DictReader(file)
    encabezados = contenido.fieldnames

    for row in contenido:
        product = row["nombre"].lower().replace(" ","")
        if productoNormalizado != product:
            filas_filtradas.append(row)

with open("inventario.csv", "w", newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames = encabezados)
    writer.writeheader()
    writer.writerows(filas_filtradas)



