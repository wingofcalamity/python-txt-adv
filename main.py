from random import randint
from models.Player import Player
from models.Enemy import Enemy
from interactions.Encounter import encounter
from data.Names import names


def create_enemy(player):
    enemy_name = names[randint(0, len(names) - 1)]
    enemy_hp = randint(3 + player.level, 15 + player.level)
    enemy_damage = randint(round(player.max_health / 20), round(player.max_health / 4))
    return Enemy(enemy_name, enemy_hp, enemy_damage)


def main():
    me = Player()
    me.autoload()
    while True:
        enemy = create_enemy(me)
        encounter(me, enemy)
        me.autosave()


if __name__ == "__main__":
    main()
