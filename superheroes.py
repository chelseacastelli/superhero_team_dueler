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
         '''Instance properties:
           abilities: List
           armors: List
           name: String
           starting_health: Integer
           current_health: Integer
         '''
         self.name = name
         self.abilities = list()
         self.armors = list()
         self.starting_health = 100
         self.current_health = current_health

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
           return: total:Int
        '''
        total = 0

        for ability in self.abilities:
            total += ability.attack()

        return total

    def add_armor(self, armor):
        ''' Add armor to self.armors
            Armor: Armor Object
        '''
        self.armors.append(armor)

    def defend(self, incoming_damage):
        '''Runs `block` method on each armor.
           Returns sum of all blocks
        '''
        total_block = 0
        if not self.armors:
            print("There are no armors")
        else:
            for armor in self.armors:
                total_block += armor.block()

            return abs(total_block - incoming_damage)

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        self.current_health -= self.defend(damage)

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.
        '''
        if self.current_health > 0:
            return True
        else:
            return False


if __name__ == "__main__":
    hero = Hero("Grace Hopper", 200)
    shield = Armor("Shield", 50)
    hero.add_armor(shield)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())
