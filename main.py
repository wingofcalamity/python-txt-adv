from models.Player import Player
from models.Enemy import Enemy


def display_help():
    print("Type 'a' to hit enemy")
    print("Type 'h' to heal yourself")
    print("Type 'i' to view encounter info")
    print("Type 's' to show your stats")


def encounter(player, enemy):
    print(f"Encountered {enemy.name}!")
    while True:
        if player.health <= 0:
            print("Game over!")
            quit()
        player_input = input(">")
        if player_input == 'a':
            player.attack(enemy)
        elif player_input == 'h':
            player.heal(enemy)
        elif player_input == 'i':
            print("+------------------+")
            print(f"| Enemy HP:  {str(enemy.health).rjust(5)} |")
            print(f"| Player HP: {str(player.health).rjust(5)} |")
            print("+------------------+")
        elif player_input == '?':
            display_help()
        elif player_input == 's':
            player.show_stats()
        elif player_input == 'w':
            enemy.roll_action(player)
        else:
            print("Type '?' to display commands")

        if enemy.health <= 0:
            break


def main():
    me = Player()
    glorb = Enemy("Glorb", 5, 3)
    glorb2 = Enemy("Blarb, Destroyer of the Universe", 25, 3)
    encounter(me, glorb)
    encounter(me, glorb2)


if __name__ == "__main__":
    main()
