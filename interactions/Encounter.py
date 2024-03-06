from Help import display_help


def encounter(player, enemy):
    print(f"Encountered {enemy.name}!")
    while True:
        if player.health <= 0:
            print("Game over!")
            quit()
        if enemy.health <= 0:
            print(f"Defeated {enemy.name}!")
            if player.xp <= 99999:
                player.xp += enemy.xp_drop
            print(f"You gained {enemy.xp_drop} XP!")
            if player.xp >= player.level_up_xp:
                player.level_up()
            break

        player_input = input(">")
        if player_input == 'a':
            player.attack(enemy)
        elif player_input == 'h':
            player.heal(enemy)
        elif player_input == 'i':
            enemy_cur_hp = str(enemy.health).rjust(5)
            enemy_max_hp = str(enemy.max_health).ljust(5)
            player_cur_hp = str(player.health).rjust(5)
            player_max_hp = str(player.max_health).ljust(5)
            print("+-------------------------+")
            print(f"| Enemy HP:   {enemy_cur_hp}/{enemy_max_hp} |")
            print(f"| Player HP:  {player_cur_hp}/{player_max_hp} |")
            print("+-------------------------+")
        elif player_input == '?':
            display_help()
        elif player_input == 's':
            player.show_stats()
        elif player_input == 'w':
            enemy.roll_action(player)
        elif player_input == '':
            continue
        else:
            print("Type '?' to display commands")
