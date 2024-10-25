import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_cover():
    print('*' * 45)
    print(' ' * 5 + '-- Adivina la Edad del Personaje --')
    print('*' * 45)
    print(' ' * 12 + '¡Buena suerte!')
    print('')

def guess_age(team_list):
    show_cover()
    character_name = input('Introduzca el nombre: ').strip().lower()
    selected_character_age = None

    for character in team_list:
        if character[0].lower() == character_name:
            selected_character_age = character[1]
            break

    if selected_character_age is None:
        print('Personaje no existe')
        return

    while True:
        age = int(input('Introduzca una edad: '))

        if age == 0:
            clear_console()
            print('Interrupción por el jugador')
            return
        
        if(age > selected_character_age):
            print(f'{character_name}, es menor.')
        elif(age < selected_character_age):
            print(f'{character_name}, es mayor.')
        else:
            print(f'Exacto, {character_name} tiene {selected_character_age}')
            return