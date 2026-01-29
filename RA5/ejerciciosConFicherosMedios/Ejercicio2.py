with open("datos.txt") as file:
    contenido = file.read()
    palabras = contenido.split(" ")

    for palabra in palabras:
        conteo = contenido.count(palabra)
        print("Frecuencia de", palabra, "es" ,conteo, "vez" if conteo == 1 else "veces")

