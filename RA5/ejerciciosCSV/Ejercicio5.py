import csv

# newline es para evitar conflicto con saltos de linea
with open("productos.csv", "w", newline='') as archivo:
    encabezado = ["Producto", "Precio", "Cantidad"]

    writer = csv.DictWriter(archivo, encabezado)
    writer.writeheader()
    writer.writerow({"Producto": "Manzana", "Precio": 1.50, "Cantidad": 100})
    writer.writerow({"Producto": "Banana", "Precio": 0.80, "Cantidad": 150})
    writer.writerow({"Producto": "Naranaja", "Precio": 0.90, "Cantidad": 120})

datos = [
    ["Nombre", "Salario", "Departamento"],
    ["Juan Pérez", 500, "Recursos Humanos"],
    ["Ana Gómez", 4200, "Marketing"],
    ["Luis Rodríguez", 2800, "Desarrollo"],
    ["María Fernández", 1900, "Finanzas"],
    ["Carlos Sánchez", 4700, "Ventas"],
    ["Sofía Torres", 3200, "Desarrollo"],
    ["Pedro Díaz", 4500, "Marketing"]
]

# Nombre del archivo CSV
archivo_csv = "empleados.csv"

# Escribir los datos en el archivo CSV
with open(archivo_csv, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(datos)

print(f"Archivo '{archivo_csv}' creado con éxito.")
