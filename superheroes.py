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
        total = 0
        if not self.armors:
            print("There are no armors")
        else:
            for armor in self.armors:
                total += armor.block()

            return total

#
# if __name__ == "__main__":
#     ability = Ability("Debugging Ability", 20)
#     print(ability.name)
#     print(ability.attack())
#
# if __name__ == "__main__":
#     armor = Armor("Shield", 12)
#     print(armor.name)
#     print(armor.block())
#
# if __name__ == "__main__":
#     hero = Hero("Grace Hopper", 200)
#     print(hero.name)
#     print(hero.current_health)
#
# if __name__ == "__main__":
#     ability = Ability("Great Debugging", 50)
#     another_ability = Ability("Flying", 70)
#     hero = Hero("Grace Hopper", 200)
#     hero.add_ability(ability)
#     hero.add_ability(another_ability)
#     print(hero.abilities)

if __name__ == "__main__":
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)

    hero = Hero("Grace Hopper", 200)

    shield = Armor("Shield", 50)

    hero.add_ability(ability)
    hero.add_ability(another_ability)
    hero.add_armor(shield)


    print(hero.defend(40))
