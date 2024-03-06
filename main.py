from models.Player import Player
from models.Enemy import Enemy
from interactions.Encounter import encounter


def main():
    me = Player()
    while True:
        glorb = Enemy("Glorb", 15, 3)
        encounter(me, glorb)


if __name__ == "__main__":
    main()
