"""
Durante el desarrollo de un pequeño videojuego se te encarga configurar y balancear cada clase
de personaje jugable. Partiendo que la estadistica base es 2, debes cumplir las siguientes
condiciones:
    ● El caballerpo tiene el doble de vida y defensa que un guerrero.
    ● El guerrero tiene el doble de ataque y alcance que un caballero.
    ● El arquero tiene la misma vida y ataque que un guerrero, pero la mitad de su defensa y el doble de su alcance
    ● Muestra como quedan las propiedades de los 3 personajes

"""
base = 2

guerrero = {
    "ataque": base,
    "alcance": base,
    "vida": base,
    "defensa": base
}

caballero = {
    "ataque": guerrero["ataque"],
    "alcance": guerrero["alcance"],
    "vida": guerrero["vida"] * 2,
    "defensa": guerrero["defensa"] * 2
}

guerrero["ataque"] = caballero["ataque"] * 2
guerrero["alcance"] = caballero["alcance"] * 2

arquero = {
    "ataque": guerrero["ataque"],
    "alcance": guerrero["alcance"] * 2,
    "vida": guerrero["vida"],
    "defensa": guerrero["defensa"] / 2
}

personajes = {
    "guerrero": guerrero,
    "caballero": caballero,
    "arquero": arquero
}
for nombre, stats in personajes.items():
    print(f"\n{nombre.upper()}")
    for atributo, valor in stats.items():
        print(f"{atributo}: {valor}")