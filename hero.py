import random
class Hero:
    """The hero blueprint will be implemented later in the project."""

    def __init__(self, name):
        self.name = name
        self.health = 115
        self.attack_power = 15
        rollRace = random.randint(1, 20)
        if rollRace <= 12:
            race = "Human"
        elif rollRace == 13:
            race = "Angel"
        elif rollRace > 13 and rollRace <= 20:
            race = "Shrek"
        self.race = race
        if race == "Angel":
            self.health = 150
            self.attack_power = 25
        if race == "Shrek":
            self.health = 125
            self.attack_power = 20
        
    def attack(self):
       if random.randint(1, 5) == 3:
           print("CRITICAL HIT")
           return random.randint(1, self.attack_power) *2
       else:
            return random.randint(1, self.attack_power)

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        return self.health > 0