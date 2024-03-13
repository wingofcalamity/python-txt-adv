from models.Player import Player
from models.Enemy import Enemy
from interactions.Encounter import encounter


def main():
    me = Player()
    me.autoload()
    while True:
        enemy = Enemy.roll_enemy(me)
        encounter(me, enemy)
        me.autosave()


if __name__ == "__main__":
    main()
