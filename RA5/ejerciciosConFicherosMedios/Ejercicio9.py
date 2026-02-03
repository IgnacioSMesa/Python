diccionario = {}

with open ("../datos.txt") as file:
    numerolinea = 1
    for linea in file:
        palabras = linea.split()

        for palabra in palabras:
            if palabra not in diccionario:
                diccionario[palabra] = []

            if numerolinea not in diccionario[palabra]:
                diccionario[palabra].append(numerolinea)

        numerolinea += 1

for palabra in diccionario:
    print(palabra, diccionario[palabra])