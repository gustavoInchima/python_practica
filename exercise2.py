def list_active_characters(tupla_team):
    return [x for x in tupla_team if x[5]]

lambda_function = lambda tuple_team : [x for x in tuple_team if x[5]]

def list_active_characters_for(tupla_team):
    list_active = []
    for i in tupla_team:
        if i[5]:
            list_active.append(i)
    return list_active

def list_active_characters_while(tuple_team):
    i = 0
    list_active = []
    while i < len(tuple_team):
        if tuple_team[i][5]:
            list_active.append(tuple_team[i])
        i += 1
    return list_active