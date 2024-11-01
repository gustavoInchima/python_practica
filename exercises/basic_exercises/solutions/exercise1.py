def average_levels_for(team_list):
    count = 0
    for character in team_list:
        count+= character[4]
    return int(count/(len(team_list)))

def average_active_character_levels_for(team_list):
    level = 0
    count = 0
    for character in team_list:
        if not character[5]:
            continue
        level += character[4]
        count += 1
    
    return int(level/count)


def average_list(team_list):
    level_list = []
    for i in range(len(team_list)):
        level_list.append(team_list[i][4])
    return int(sum(level_list)/len(team_list))


def average_compact(team_list):
    return sum([x[4] for x in team_list])//len(team_list)


def average_active_character(item_list):
    active_team_list = [x[4] for x in item_list if x[5]]
    return sum(active_team_list)//len(active_team_list)




