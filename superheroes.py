import random


class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        ''' Return a value between 0 and the initialized max_damage strength.'''
        return random.randint(0, self.max_damage)


class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        ''' Return a random value between 0 and the initialized max_block strength. '''
        return random.randint(0, self.max_block)


class Hero:
    def __init__(self, name, current_health):
        self.name = name
        self.abilities = []
        self.armors = []
        self.starting_health = 100
        self.current_health = current_health
        

if __name__ == "__main__":
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())

if __name__ == "__main__":
    armor = Armor("Shield", 12)
    print(armor.name)
    print(armor.block())

if __name__ == "__main__":
    hero = Hero("Grace Hopper", 200)
    print(hero.name)
    print(hero.current_health)
