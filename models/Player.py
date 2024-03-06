import random


class Player:
    def __init__(self):
        self.level = 1
        self.health = 20
        self.max_health = 20
        self.min_damage = 1
        self.max_damage = 5
        self.min_heal = 5
        self.max_heal = 15
        self.hit_chance = 95
        self.crit_chance = 5
        self.xp = 0
        self.level_up_xp = 30

    def attack(self, enemy):
        if random.randint(1, 100) <= self.hit_chance:
            damage = random.randint(self.min_damage, self.max_damage)
            if enemy.health >= 0:
                if random.randint(1, 100) <= self.crit_chance:
                    print("Critical hit!")
                    crit_damage = self.max_damage * 2.5
                    damage = round(crit_damage)
                enemy.health -= damage
                print(f"Hit {enemy.name} for {damage} damage!")
                if enemy.health > 0:
                    enemy.roll_action(self)

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
        max_damage = str(self.max_damage).rjust(3)
        min_heal = str(self.min_heal).rjust(3)
        max_heal = str(self.max_heal).rjust(3)
        hit_chance = str(self.hit_chance).rjust(3)
        crit_chance = str(self.crit_chance).rjust(3)
        level = str(self.level).rjust(3)
        xp = str(self.xp).rjust(5)
        left = str(self.level_up_xp).ljust(5)
        print("+------Player stats:------+")
        print(f"| Level:         {level}      |")
        print(f"| XP:         {xp}/{left} |")
        print("+-------------------------+")
        print(f"| Hit chance:        {hit_chance}% |")
        print(f"| Crit chance:       {crit_chance}% |")
        print(f"| Damage:       {min_damage} ~ {max_damage} |")
        print(f"| Healing:      {min_heal} ~ {max_heal} |")
        print("+-------------------------+")

    def level_up(self):
        print("You leveled up!")
        # what even is scaling
        old_max_health = self.max_health
        self.level += 1
        self.max_health += 2
        self.health += (old_max_health - self.max_health)
        self.min_damage += 1
        self.max_damage += 2
        self.min_heal += 1
        self.max_heal += 2
        self.crit_chance += 2
        # resetting xp, increasing cost
        self.xp = 0
        self.level_up_xp = round(self.level_up_xp * 1.5)
