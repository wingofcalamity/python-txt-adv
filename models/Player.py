import random


class Player:
    def __init__(self):
        self.health = 20
        self.max_health = 20
        self.min_damage = 1
        self.max_damage = 5
        self.min_heal = 5
        self.max_heal = 15
        self.hit_chance = 95
        self.crit_chance = 5

    def attack(self, enemy):
        if random.randint(0, 100) < self.hit_chance:
            damage = random.randint(self.min_damage, self.max_damage)
            enemy.health -= damage
            if enemy.health >= 0:
                if random.randint(0, 100) <= self.crit_chance:
                    print("Critical hit!")
                    crit_damage = self.max_damage * 2.5
                    damage = round(crit_damage)
                print(f"Hit {enemy.name} for {damage} damage!")
                enemy.roll_action(self)
            else:
                print(f"Hit {enemy.name} for {damage} damage!")
                print(f"Defeated {enemy.name}!")

    def heal(self, enemy):
        heal_rate = random.randint(self.min_heal, self.max_heal)
        if self.health == self.max_health:
            print("Your HP are full.")
        elif self.health + heal_rate > self.max_health:
            print(f"Healed yourself for {self.max_health - self.health} HP")
            self.health = self.max_health
        else:
            print(f"Healed yourself for {heal_rate} HP")
            self.health += heal_rate
        enemy.roll_action(self)

    def show_stats(self):
        min_damage = str(self.min_damage).rjust(3)
        max_damage = str(self.max_damage).ljust(3)
        min_heal = str(self.min_heal).rjust(3)
        max_heal = str(self.max_heal).ljust(3)
        hit_chance = str(self.hit_chance).rjust(3)
        crit_chance = str(self.crit_chance).rjust(3)
        print("Player stats:")
        print(f"Hit chance:   {hit_chance}%")
        print(f"Crit chance:  {crit_chance}%")
        print(f"Damage:    {min_damage} ~ {max_damage}")
        print(f"Healing:   {min_heal} ~ {max_heal}")
        print()