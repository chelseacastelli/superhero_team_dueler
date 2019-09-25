
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


if __name__ == "__main__":
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())

    armor = Armor("Shield", 12)
    print(armor.name)
    print(armor.block())
