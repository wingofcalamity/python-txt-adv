from random import randint

from models.Player import Player
from models.Enemy import Enemy
from interactions.Encounter import encounter
from data.Names import names


def create_enemy():
    enemy_name = names[randint(0, len(names) - 1)]
    enemy_hp = randint(3, 15)
    enemy_damage = randint(1, 5)
    return Enemy(enemy_name, enemy_hp, enemy_damage)


def main():
    me = Player()
    while True:
        enemy = create_enemy()
        encounter(me, enemy)


if __name__ == "__main__":
    main()
