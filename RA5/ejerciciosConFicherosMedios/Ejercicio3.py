palabraBuscar = input("Ingrese una palabra que quiere: ")

with open("datos.txt", encoding="utf-8") as file:

    for linea in file:
        if palabraBuscar in linea:
            print(linea.strip())