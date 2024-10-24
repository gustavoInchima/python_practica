from exercise1 import *

# Esta base de datos está organizada como una lista de tuplas
 # cada tupla representa un personaje y contiene los siguientes datos: 
'''
    Nombre
    Edad
    Clase, 
    Raza, 
    Nivel,
    booleano, indica si el personaje está en el equipo.
 '''

personajes_principales = [
    ("Astarion", 239, "Rogue", "Elf", 3, True),
    ("Shadowheart", 40, "Cleric", "Half-Elf", 5, True),
    ("Wyll", 25, "Warlock", "Human", 2, False),
    ("Gale", 35, "Wizard", "Human", 5, True),
    ("Karlach", 32, "Barbarian", "Tiefling", 6, False),
    ("Lae'zel", 20, "Fighter", "Githyanki", 4, True),
    ("Jaheira", 150, "Druid", "Half-Elf", 6, False),
    ("Halsin", 350, "Druid", "Elf", 7, False),
    ("Minsc", 130, "Ranger", "Human", 5, False),
    ("Minthara", 250, "Paladin", "Drow", 8, False),
    ("Dark Urge", 30, "Sorcerer", "Dragonborn", 1, False)
]

""""
Ejercicio 1: Calcular el nivel medio del equipo (1 Punto)

Escribe una función que calcule el nivel medio del equipo, devolviendo la parte entera.
"""

print(average_active_character_levels_for(personajes_principales))
print(average_levels_for(personajes_principales))
print(average_list(personajes_principales))
print(average_compact(personajes_principales))
print(average_active_character(personajes_principales))

