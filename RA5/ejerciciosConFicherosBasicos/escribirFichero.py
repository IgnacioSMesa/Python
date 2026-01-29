listaPalabras = []
palabra = ""

while palabra != "fin":

    try:

        palabra = input("Ingrese una palabra, fin para terminar: ")
        listaPalabras.append(palabra)

    except ValueError:
        print("Ingrese un valor valido")

with open('pruebaEscritura.txt', 'w') as file:
    for palabra in listaPalabras:
        file.write(palabra + " ")
