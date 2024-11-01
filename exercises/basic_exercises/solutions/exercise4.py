def character_for_raza(list_team):
    dict_raza = {}
    for i in list_team:
        raza = i[3]
        if raza not in dict_raza.keys():
            dict_raza[raza] = 1
        else:
            dict_raza[raza] += 1
    return dict_raza

def character_for_raza_2(list_team):
    dict_race = {}
    for character in list_team:
        race = character[3]
        dict_race[race] = dict_race.get(race, 0) +1
    return dict_race