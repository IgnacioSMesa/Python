import csv

jefes = [
    # Cruces Olvidados
    {"nombre": "Falso Caballero", "tipo": "Jefe", "localizacion": "Cruces Olvidados", "promedio_derrotas": 4.2},
    {"nombre": "Rey Vengamoscas", "tipo": "Mini Jefe", "localizacion": "Cruces Olvidados", "promedio_derrotas": 1.5},
    {"nombre": "Gruz Madre", "tipo": "Mini Jefe", "localizacion": "Cruces Olvidados", "promedio_derrotas": 1.2},

    # Sendero Verde
    {"nombre": "Hornet (Protector)", "tipo": "Jefe", "localizacion": "Sendero Verde", "promedio_derrotas": 2.0},

    # Yermos Fúngicos
    {"nombre": "Señores Mantis", "tipo": "Jefe", "localizacion": "Aldea Mantis", "promedio_derrotas": 6.5},
    {"nombre": "Defensor del Estiércol", "tipo": "Jefe", "localizacion": "Vía Real", "promedio_derrotas": 3.8},

    # Ciudad de Lágrimas
    {"nombre": "Maestro del Alma", "tipo": "Jefe", "localizacion": "Ciudad de Lágrimas", "promedio_derrotas": 5.1},
    {"nombre": "Tirano del Alma", "tipo": "Jefe de Sueño", "localizacion": "Ciudad de Lágrimas", "promedio_derrotas": 4.7},
    {"nombre": "Vigilantes", "tipo": "Jefe", "localizacion": "Ciudad de Lágrimas", "promedio_derrotas": 6.9},

    # Cuenca Antigua
    {"nombre": "Caballero Centinela", "tipo": "Jefe", "localizacion": "Cuenca Antigua", "promedio_derrotas": 3.2},

    # Jardines de la Reina
    {"nombre": "Traidor Lord", "tipo": "Jefe", "localizacion": "Jardines de la Reina", "promedio_derrotas": 7.4},

    # Cañón de Niebla
    {"nombre": "Uumuu", "tipo": "Jefe", "localizacion": "Cañón de Niebla", "promedio_derrotas": 3.9},

    # Nido Profundo
    {"nombre": "Bestia Acechante", "tipo": "Jefe", "localizacion": "Nido Profundo", "promedio_derrotas": 2.8},
    {"nombre": "Nosk", "tipo": "Jefe", "localizacion": "Nido Profundo", "promedio_derrotas": 5.6},

    # Borde del Reino
    {"nombre": "Hornet (Centinela)", "tipo": "Jefe", "localizacion": "Borde del Reino", "promedio_derrotas": 6.1},

    # Colmena
    {"nombre": "Caballero de la Colmena", "tipo": "Jefe", "localizacion": "Colmena", "promedio_derrotas": 4.4},

    # DLC / Sueño
    {"nombre": "Príncipe Gris Zote", "tipo": "Jefe de Sueño", "localizacion": "Sueño", "promedio_derrotas": 12.7},
    {"nombre": "Rey Pesadilla Grimm", "tipo": "Jefe DLC", "localizacion": "Sueño", "promedio_derrotas": 9.3},
    {"nombre": "Grimm", "tipo": "Jefe DLC", "localizacion": "Distrito del Circo", "promedio_derrotas": 6.0},
    {"nombre": "Guardían Cristalizado", "tipo": "Jefe", "localizacion": "Pico Cristal", "promedio_derrotas": 4.9},
    {"nombre": "Guardían Cristalizado Enfurecido", "tipo": "Jefe de Sueño", "localizacion": "Pico Cristal", "promedio_derrotas": 7.8},

    # Finales
    {"nombre": "Hollow Knight", "tipo": "Jefe Final", "localizacion": "Templo del Huevo Negro", "promedio_derrotas": 3.5},
    {"nombre": "Radiance", "tipo": "Jefe Final Secreto", "localizacion": "Sueño", "promedio_derrotas": 10.2},
    {"nombre": "Radiance Absoluta", "tipo": "Jefe Final DLC", "localizacion": "Panteón de Hallownest", "promedio_derrotas": 25.0}
]

# Crear el archivo CSV
with open("jefes_hollow_knight.csv", mode="w", newline="", encoding="utf-8") as archivo:
    campos = ["nombre", "tipo", "localizacion", "promedio_derrotas"]
    writer = csv.DictWriter(archivo, fieldnames=campos)

    writer.writeheader()
    writer.writerows(jefes)

print("CSV creado correctamente.")
