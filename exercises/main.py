from solutions.exercise1 import *
from solutions.exercise2 import *
from solutions.exercise3 import *
from solutions.exercise4 import *
from solutions.exercise7 import *
from solutions.exercise8 import guess_age

# Esta base de datos está organizada como una lista de tuplas
'''
Cada tupla representa un personaje y contiene los siguientes datos: 
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

#print(average_active_character_levels_for(personajes_principales))
# print(average_levels_for(personajes_principales))
# print(average_list(personajes_principales))
# print(average_compact(personajes_principales))
# print(average_active_character(personajes_principales))


"""
Ejercicio 2: Filtrar personajes en el equipo (1 Punto)

Escribe una función que devuelva una lista con los personajes que actualmente están en el equipo.
"""

#print(list_active_characters(personajes_principales))
#print(list_active_characters_for(personajes_principales))
#print(lambda_function(personajes_principales))
#print(list_active_characters_while(personajes_principales))

'''
Ejercicio 3: Conjunto de clases únicas (1 Punto)

Escribe una función para crear una estructura con todas las clases únicas de los personajes, no puede haber elementos repetidos.
'''
#print(lambda_func(personajes_principales))
#print(get_clases(personajes_principales))
#print(get_clases_for(personajes_principales))
#print(get_classes_without_set(personajes_principales))

"""
Ejercicio 4: Conteo de Personajes por Raza (1 Punto)

Escribe una función que cuente cuántos personajes hay de cada raza y devuelva esta información en forma de diccionario.
"""

#print(character_for_raza(personajes_principales))
#print(character_for_raza_2(personajes_principales))

'''
Ejercicio 5: Verificación de Existencia de Raza (1 Punto)

Escribe una función que verifique si existe al menos un personaje de una raza específica en la lista, devolviendo True o False. 
La búsqueda debe detenerse tan pronto como se encuentre un personaje de la raza indicada.
'''

def find_raza(raza, list_team):
    for i in list_team:
        if i[3] == raza:
            return True
    return False

#print(find_raza('Elfi', personajes_principales))
#print(find_raza('Elf', personajes_principales))


"""
Ejercicio 6: Personaje con Mayor Nivel (1.5 Puntos)

Escribe una función que encuentre el nombre del primer personaje de mayor nivel dentro de una clase especificada. 
El parámetro de la clase debe tener un valor por defecto de None, permitiendo que, si no se especifica una clase, 
la función devuelva el nombre del personaje con mayor nivel general.
"""

def find_stronger_character(team_list, class_name = None):
    match_list = [x for x in team_list if class_name is None or x[2] == class_name]
    if not match_list:
        return None
    return max(match_list, key=lambda x:x[4])[0]
    

# print(find_stronger_character(personajes_principales, 'Druid'))
# print(find_stronger_character(personajes_principales, 'fake'))
# print(find_stronger_character(personajes_principales))


"""
Ejercicio 7: Incrementar Nivel de un Personaje (1.5 Puntos)

Escribe una función que, dado un nombre, incremente en uno el nivel del personaje correspondiente sin devolver nada.
"""

#print(personajes_principales)
#print(upgrade_character_level("Gale", personajes_principales))
#print(personajes_principales)
#print(upgrade_character_level_enumerate("Gale", personajes_principales))

"""
Ejercicio 8: Programa un juego - Adivina la edad del personaje (2 Puntos)

Solicita por consola el nombre de un personaje. Luego haz que introduzca una edad hasta acertar con la edad del personaje cuyo nombre sea igual al introducido. 
Debe informar si acierta, o si el personaje es mayor o menor a la edad introducida. Además, si la edad introducida es 0, haz que termine el juego inmediatamente 
con el siguiente mensaje “Interrupción por el jugador”.
"""

print(guess_age(personajes_principales))