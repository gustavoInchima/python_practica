def upgrade_character_level(character_name, team_list):
    level_index = 4
    for i in range(len(team_list)):
        if team_list[i][0] == character_name:
            # Convertimos la tupla a lista para poder modificarla
            character_data = list(team_list[i])
            character_data[level_index] +=1
            # Actualizamos la lista del equipo con la nueva tupla
            team_list[i] = tuple(character_data)
            break

def upgrade_character_level_enumerate(character_name, team_list):
    for i, character in enumerate(team_list):
        if character[0] == character_name:
            team_list[i] = character[:4] + (character[4]+1,) + character[4+1:]