thisdict = {
  "datos": {
    "nombre" : "Ignacio",
    "apellido" : "Sanz"
  },
  "curso": "2DAM",
  "edad": 21,
}

# Imprime todo el diccionario
print(thisdict)

# Acceder a elementos dentro de un diccionario anidado
print(thisdict["datos"]["nombre"])
print(thisdict["datos"]["apellido"])

# Obtener un valor con get
print(thisdict.get("datos"))

# Ver todas las claves del diccionario
print(thisdict.keys())

# añadir una clave con un valor al diccionario
thisdict["annioNacimiento"] = 2004
print(thisdict)

# actualizar un campo, en este caso nos metemos dentro de datos
thisdict["datos"].update({"nombre" : "Natalia"})
print(thisdict)

#borrar elementos guardando el elemento
#thisdict.pop("curso")
#print(thisdict)

# borrar elementos sin guardar el elemento
#del thisdict["annioNacimiento"]

# vaciar diccionario
#thisdict.clear()
print(thisdict)

# 1. Recorrer todas las claves
print("Claves:")
for clave in thisdict:
    print(clave)

# 2. Recorrer todas las claves usando keys()
print("\nClaves usando keys():")
for clave in thisdict.keys():
    print(clave)

# 3. Recorrer todos los valores
print("\nValores:")
for valor in thisdict.values():
    print(valor)

# 4. Recorrer claves y valores al mismo tiempo
print("\nClaves y valores:")
for clave, valor in thisdict.items():
    print(clave, ":", valor)

# 5. Recorrer un diccionario anidado
print("\nDiccionario anidado 'datos':")
for clave, valor in thisdict["datos"].items():
    print(clave, ":", valor)