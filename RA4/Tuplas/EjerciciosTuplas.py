"""
Ejercicio 1: Crea una función calcular_estadisticas(numeros) que reciba una lista de
números y devuelva una tupla con:
● El valor mínimo.
● El valor máximo.
● La media aritmética.

"""
import math


def calcular_estadisticas(*numeros):
    return min(numeros), max(numeros), sum(numeros)/len(numeros)

# print(calcular_estadisticas(1, 2, 3))

"""
Ejercicio 2: Crea una función distancia(p1, p2) que reciba dos tuplas representando
puntos en el plano (x, y) y devuelva la distancia entre ellos usando la fórmula:
"""

def distancia(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

d = distancia((1, 2), (4, 6))
# print(d)

"""
Ejercicio 3: Crea una función analizar_texto(texto) que devuelva una tupla con:
● Número total de caracteres.
● Número de palabras.
● Primera palabra del texto.
"""

def analizar_texto(texto):
    return len(texto), len(texto.split()), texto.split()[0]

# print(analizar_texto('Hola mundo desde 2dam'))

"""
Ejercicio 4: Crea una función convertir_temperatura(celsius) que reciba una
temperatura en grados Celsius y devuelva una tupla con:
● La temperatura en Fahrenheit.
● La temperatura en Kelvin.
"""

def convertir_temperatura(celsius):
    return (celsius * 9 / 5) + 32, celsius + 273

# print(convertir_temperatura(5))

"""
Ejercicio 5: Crea una función analizar_numeros(numeros) que reciba una lista de
enteros y devuelva una tupla con:
● El número de elementos pares.
● El número de elementos impares.
● La suma total.
"""

def analizar_numeros(numeros):

    numerosPares = 0
    numerosImpares = 0

    for numero in numeros:
        if numero % 2 == 0:
            numerosPares += 1
        else:
            numerosImpares += 1

    return numerosPares, numerosImpares, sum(numeros)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(analizar_numeros(numeros))

"""
Ejercicio 6: Crea una función procesar_cadena(cadena) que devuelva una tupla con:
● La cadena en mayúsculas.
● La cadena en minúsculas.
● La longitud de la cadena.
"""

def procesar_cadena(cadena):
    return cadena.upper(), cadena.lower(), len(cadena)

# print(procesar_cadena("hola mundo"))