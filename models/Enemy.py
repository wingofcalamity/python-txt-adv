import random


class Enemy:
    def __init__(self, name, health, max_damage):
        self.max_health = health
        self.health = health
        self.hit_chance = 66
        self.name = name
        self.max_damage = max_damage
        self.xp_drop = round((max_damage * health) / 5)

    def roll_action(self, player):
        if random.randint(1, 100) <= self.hit_chance:
            damage = random.randint(1, self.max_damage)
            print(f"{self.name} hit you for {damage} damage!")
            player.health -= damage
        else:
            print(f"{self.name} did nothing.")
