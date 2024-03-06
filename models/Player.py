import random


class Player:
    def __init__(self):
        self.level = 1
        self.health = 20
        self.max_health = 20
        self.min_damage = 3
        self.max_damage = 6
        self.min_heal = 6
        self.max_heal = 12
        self.hit_chance = 100
        self.crit_chance = 5
        self.xp = 0
        self.level_up_xp = 30
        self.defeated_enemies = 0

    def reset(self):
        self.level = 1
        self.health = 20
        self.max_health = 20
        self.min_damage = 3
        self.max_damage = 6
        self.min_heal = 6
        self.max_heal = 12
        self.hit_chance = 100
        self.crit_chance = 5
        self.xp = 0
        self.level_up_xp = 30
        self.defeated_enemies = 0

    def attack(self, enemy):
        hit_roll = random.randint(1, 100)
        if hit_roll <= self.hit_chance:
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
                else:
                    self.defeated_enemies += 1
                    print(f"Defeated {enemy.name}!")
                    self.xp += enemy.xp_drop
                    print(f"You gained {enemy.xp_drop} XP!")
                    if self.xp >= self.level_up_xp:
                        self.level_up()
                    print()
        else:
            print(f"You missed! {hit_roll}")
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
        crit_chance = str(self.crit_chance).rjust(5)
        level = str(self.level).rjust(3)
        xp = str(self.xp).rjust(5)
        left = str(self.level_up_xp).ljust(5)
        wins = str(self.defeated_enemies).rjust(5)
        print("+------Player stats:------+")
        print(f"| Level:         {level}      |")
        print(f"| XP:         {xp}/{left} |")
        print(f"| Wins:             {wins} |")
        print("+-------------------------+")
        print(f"| Hit chance:        {hit_chance}% |")
        print(f"| Crit chance:     {crit_chance}% |")
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
        self.crit_chance += .5
        # resetting xp, increasing cost
        self.xp = 0
        self.level_up_xp = round(self.level_up_xp * 1.5)

    def stat_dump(self):
        return [
            self.level,
            self.health,
            self.max_health,
            self.min_damage,
            self.max_damage,
            self.min_heal,
            self.max_heal,
            self.hit_chance,
            self.crit_chance,
            self.xp,
            self.level_up_xp,
            self.defeated_enemies
        ]

    def set_stats(self, stat_list):
        self.level = int(stat_list[0])
        self.health = int(stat_list[1])
        self.max_health = int(stat_list[2])
        self.min_damage = int(stat_list[3])
        self.max_damage = int(stat_list[4])
        self.min_heal = int(stat_list[5])
        self.max_heal = int(stat_list[6])
        self.hit_chance = int(stat_list[7])
        self.crit_chance = float(stat_list[8])
        self.xp = int(stat_list[9])
        self.level_up_xp = int(stat_list[10])
        self.defeated_enemies = int(stat_list[11])

    def autosave(self):
        with open("./data/save", 'w') as file:
            for item in self.stat_dump():
                file.write("%s\n" % item)

    def autoload(self):
        try:
            with open("./data/save", 'r') as file:
                loaded_list = [line.strip() for line in file]
                if len(loaded_list) == 12:
                    self.set_stats(loaded_list)
        except Exception as e:
            print(f"Failed to load Data: {e}")
