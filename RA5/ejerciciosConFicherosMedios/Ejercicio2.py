frecuencias = {}

with open("datos.txt") as file:
    contenido = file.read()
    palabras = contenido.split(" ")

    for palabra in palabras:
        for palabra in palabras:
            if palabra in frecuencias:
                frecuencias[palabra] += 1
            else:
                frecuencias[palabra] = 1

for palabra, conteo in frecuencias.items():
    print("Frecuencia de", palabra, "es", conteo, "vez" if conteo == 1 else "veces")

