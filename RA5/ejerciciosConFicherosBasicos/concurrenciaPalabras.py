palabra = input("Ingrese una palabra: ")

with open ("datos.txt", "r") as file:
    contenido = file.read().count(palabra)

print("La palabra", palabra, "aparece", contenido)