"""
Tienes una lista de productos.
Cada producto es una tupla con esta estructura:

(nombre, precio, stock)

Datos iniciales

productos = [
    ("Portatil", 1200, 5),
    ("Raton", 25, 50),
    ("Teclado", 80, 20),
    ("Monitor", 300, 10),
    ("USB", 10, 100)
]
1. Ordena los productos por precio (de menor a mayor).
2. Ordena los productos por stock (de mayor a menor).
3. Ordena los productos por nombre alfabéticamente.

Pista: puedes usar lambda o itemgetter en el key
"""
productos = [
    ("Portatil", 1200, 5),
    ("Raton", 25, 50),
    ("Teclado", 80, 20),
    ("Monitor", 300, 10),
    ("USB", 10, 100)
]

# Con lambda

# 1
productos_por_precio = sorted(productos, key=lambda p: p[1])
print(productos_por_precio)

#2
productos_por_stock = sorted(productos, key=lambda p: p[2], reverse=True)
print(productos_por_stock)

#3
productos_por_nombre = sorted(productos, key=lambda p: p[0])
print(productos_por_nombre)

print("\n")
# Sin lambda

"""
itemgetter es una función del módulo estándar operator de Python que se usa para extraer uno o varios 
elementos de un objeto (listas, tuplas, diccionarios, etc.).
Se utiliza mucho como alternativa a lambda, sobre todo al ordenar.
"""
from operator import itemgetter

productos_por_precio = sorted(productos, key=itemgetter(1))
print(productos_por_precio)

productos_por_stock = sorted(productos, key=itemgetter(2), reverse=True)
print(productos_por_stock)

productos_por_nombre = sorted(productos, key=itemgetter(0))
print(productos_por_nombre)

