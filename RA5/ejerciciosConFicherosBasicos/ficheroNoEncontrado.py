try:
    with open ("datos.txt", "r") as file:
        contenedor = file.read()

except FileNotFoundError:
    print("No encontrado")