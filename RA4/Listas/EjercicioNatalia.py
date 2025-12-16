"""
Se dispone de una lista de números enteros llamada lista.

lista = [60, 3, 12, 7, 55]

Se pide escribir un programa en Python que ordene la lista
utilizando una función personalizada como clave de ordenamiento,
cumpliendo las siguientes reglas:
Si el número es par, su valor de comparación será la mitad del número.
Si el número es impar, su valor de comparación será el doble del número.

Consigna:
Define una función que reciba un número entero y devuelva el valor que se usará como criterio para ordenar.
Utiliza dicha función como argumento key del método sort() para ordenar la lista.
Muestra la lista ordenada por pantalla.

"""
def ordenarLista(n):
    if n % 2 == 0:
        return n / 2
    else:
        return n * 2

lista = [60, 3, 12, 7, 55]
lista.sort(key=ordenarLista)
print(lista)