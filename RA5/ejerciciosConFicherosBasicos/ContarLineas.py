try:
    with open ("datos.txt") as file:
        lineas = file.readlines()
        numeroLineas = len(lineas)

        print("Tiene", numeroLineas, "lineas")

except FileNotFoundError:
    print("No hay lineas")