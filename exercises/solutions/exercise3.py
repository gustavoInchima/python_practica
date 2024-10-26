lambda_func = lambda tuple_team : set([x[2] for x in tuple_team])

def get_clases(tuple_team):
    return set([x[2] for x in tuple_team])

def get_clases_for(tuple_team):
    classes_set = set()
    for character in tuple_team:
        classes_set.add(character[2])
    return classes_set

def get_classes_without_set(tuple_team):
    classes_list = []
    for character in tuple_team:
        if character[2] not in classes_list:
            classes_list.append(character[2])
    return classes_list

