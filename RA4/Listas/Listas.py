cadena = "navidad"
#cadena[2] = 'o' las cadenas son inmutables, no se pueden modificar caracter a caracter
"""
Si quieres cambiar una letra, debes crear una nueva cadena:
cadena = cadena[:2] + 'o' + cadena[3:]
"""


lista = [1, "feliz", "feliz", "navidad", 4.6, [33,66]]
print(lista[-1]) # saca el ultimo elemento
print(lista[2:5]) # sacamo un rango del 2 al 4, el ulitmo no lo saca
print(lista[:4]) # empieza desde el 0 hasta el cuarto
print(lista[-4,-1]) # desde el ultimo, sin incluirlo, hasta el -4, va al reves
print() # sacamos los 4 primeros
lista[2] = "2026" # las listas en cambio si son mutables
print(lista)
print(list(range(1,10,2))) # empieza en 1, termina en 10 sin incluirse, por pasos de 2
line = "A lot        of spaces"