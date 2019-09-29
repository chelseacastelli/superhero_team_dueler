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

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        if not self.abilities and not opponent.abilities:
            print("Draw")

        while self.is_alive() and opponent.is_alive():
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())

        if self.is_alive():
            print(f"{self.name} won!")
        else:
            print(f"{opponent.name} won!")


class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        return random.randint(self.max_damage//2, self.max_damage)















# if __name__ == "__main__":
#     hero1 = Hero("Wonder Woman", 200)
#     hero2 = Hero("Dumbledore", 200)
#     shield = Armor("Shield", 50)
#     suit = Armor("Suit", 30)
#     hero1.add_armor(suit)
#     hero2.add_armor(shield)
#     ability1 = Ability("Super Speed", 300)
#     ability2 = Ability("Super Eyes", 130)
#     ability3 = Ability("Wizard Wand", 80)
#     ability4 = Ability("Wizard Beard", 20)
#     hero1.add_ability(ability1)
#     hero1.add_ability(ability2)
#     hero2.add_ability(ability3)
#     hero2.add_ability(ability4)
#     hero1.fight(hero2)
