import random
from data.Names import names
from random import randint

enemy_types = ["Normal", "Water", "Fire", "Nature", "Light", "Dark"]
type_amount = len(enemy_types) - 1


class Enemy:
    def __init__(self, name, health, max_damage, enemy_type):
        self.max_health = health
        self.health = health
        self.hit_chance = 66
        self.name = name
        self.type = enemy_type
        self.max_damage = max_damage
        self.xp_drop = round((max_damage * health) / 5)

    @staticmethod
    def roll_enemy(player):
        name = names[randint(0, len(names) - 1)]
        health = randint(1, 10)
        max_damage = randint(1, 10)
        enemy_type = randint(0, type_amount)
        return Enemy(
            name,
            health,
            max_damage,
            enemy_types[enemy_type]
        )

    def roll_action(self, player):
        if random.randint(1, 100) <= self.hit_chance:
            damage = random.randint(1, self.max_damage)
            print(f"{self.name} hit you for {damage} damage!")
            player.health -= damage
        else:
            print(f"{self.name} did nothing.")
