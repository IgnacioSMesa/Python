palabra = input("Ingrese la palabra que quiere: ")
palabraReemplazar = ("Python")

with open("datos.txt", encoding="utf-8") as file:
   contenido = file.read()

contenidoModificado = contenido.replace(palabraReemplazar, palabra)

with open("modificaciones.txt", "w") as file:
    file.write(contenidoModificado)