from interactions.Help import display_help
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def type_message(e_type):
    if e_type == "Water":
        return "Wet "
    elif e_type == "Fire":
        return "Fiery "
    elif e_type == "Light":
        return "Radiant "
    elif e_type == "Dark":
        return "Emo "
    elif e_type == "Nature":
        return "Green "
    return ""


def encounter(player, enemy):
    print(f"Encountered {type_message(enemy.type)}{enemy.name}")
    print(f"HP: {enemy.health} ATK: {enemy.max_damage}")
    while True:
        if player.health <= 0:
            print("Game over!")
            quit()
        if enemy.health <= 0:
            break

        player_input = input('>')

        if player_input == 'a':
            player.attack(enemy)
        elif player_input == 'h':
            player.heal(enemy)
        elif player_input == 'i':
            enemy_cur_hp = str(enemy.health).rjust(5)
            enemy_max_hp = str(enemy.max_health).ljust(5)
            player_cur_hp = str(player.health).rjust(5)
            player_max_hp = str(player.max_health).ljust(5)
            player_cur_mp = str(player.mana).rjust(5)
            player_max_mp = str(player.max_mana).ljust(5)
            enemy_type = enemy.type.ljust(8)
            print("+-------------------------+")
            print(f"| Enemy HP:   {enemy_cur_hp}/{enemy_max_hp} |")
            print(f"| Enemy Type:    {enemy_type} |")
            print("+-------------------------+")
            print(f"| Player HP:  {player_cur_hp}/{player_max_hp} |")
            print(f"| Player MP:  {player_cur_mp}/{player_max_mp} |")
            print("+-------------------------+")
        elif player_input == '?':
            display_help()
        elif player_input == 's':
            player.show_stats()
        elif player_input == 'c':
            clear_screen()
        elif player_input == 'w':
            enemy.roll_action(player)
        else:
            print("Unrecognized command.")
            print("Type '?' to display commands.")
