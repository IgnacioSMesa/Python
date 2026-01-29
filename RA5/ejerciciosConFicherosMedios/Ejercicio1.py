with open ("datos.txt") as file:
    palabras = file.read().split()
    print(f"El archivo contiene {len(palabras)} palabras")