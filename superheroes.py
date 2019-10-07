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
    def __init__(self, name, current_health=100):
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
         self.starting_health = current_health
         self.current_health = current_health
         self.deaths = 0
         self.kills = 0


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

    def add_kills(self, num_kills):
        ''' Update kills with num_kills'''
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        ''' Update deaths with num_deaths'''
        self.deaths += num_deaths

    def add_armor(self, armor):
        ''' Add armor to self.armors
            Armor: Armor Object
        '''
        self.armors.append(armor)

    def defend(self, incoming_damage=0):
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
        return int(self.current_health) > 0

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        if not self.abilities and not opponent.abilities:
            print("Draw")

        while self.is_alive() and opponent.is_alive():
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())

        if self.is_alive():
            opponent.add_deaths(1)
            self.add_kills(1)
            print(f"{self.name} won!")
        else:
            opponent.add_kills(1)
            self.add_deaths(1)
            print(f"{opponent.name} won!")

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        self.abilities.append(weapon)

    def add_armor(self, armor):
        '''Add Armor to self.armors
            armor: Armor Object
        '''
        self.armors.append(armor)

class Arena:
    def __init__(self):
         '''Instantiate properties
            team_one: None
            team_two: None
         '''
         self.team_one = None
         self.team_two = None

    def create_ability(self):
        '''Prompt for Ability information.
           return Ability with values from user Input
        '''
        abil = input("Ability name: ")
        dmg = int(input("Max damage: "))
        return Ability(abil, dmg)

    def create_weapon(self):
        '''Prompt user for Weapon information
           return Weapon with values from user input.
        '''
        weap = input("Weapon name: ")
        dmg = int(input("Max damage: "))
        return Weapon(weap, dmg)

    def create_armor(self):
        '''Prompt user for Armor information
           return Armor with values from user input.
        '''
        arm = input("Armor name: ")
        block = int(input("Max block: "))
        return Armor(arm, block)

    def create_hero(self):
        '''Prompt user for Hero information
           return Hero with values from user input.
        '''
        hero_name = input("Hero name: ")
        health = int(input("Health: "))
        hero = Hero(hero_name, health)

        abilities = input("Add ability? (y/n) ")
        if abilities.lower() == 'y':
            while True:
                ability = self.create_ability()
                hero.add_ability(ability)
                another = input("Another ability? (y/n) ")
                if another.lower() != 'y':
                    break

        weapons = input("Add weapon? (y/n) ")
        if weapons.lower() == 'y':
            while True:
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
                another = input("Another weapon? (y/n) ")
                if another.lower() != 'y':
                    break

        armors = input("Add armor? (y/n) ")
        if armors.lower() == 'y':
            while True:
                armor = self.create_armor()
                hero.add_armor(armor)
                another = input("Another armor? (y/n) ")
                if another.lower() != 'y':
                    break

        return hero

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        team_name = input("Team name: ")
        number_of_heroes = input("How many heroes? ")
        self.team_one = Team(team_name)

        for _ in range(int(number_of_heroes)):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        '''Prompt the user to build team_two '''
        team_name = input("Team name: ")
        number_of_heroes = input("How many heroes? ")
        self.team_two = Team(team_name)

        for _ in range(int(number_of_heroes)):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        self.team_one.attack(self.team_two)

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        team_one_stats = self.team_one.stats()
        team_two_stats = self.team_two.stats()

        if team_one_stats > team_two_stats:
            print(f"{self.team_one.name} wins!")
            print("Still alive:\n")
            for hero in self.team_one.heroes:
                print(f"{hero.name}")
        elif team_one_stats < team_two_stats:
            print(f"{self.team_two.name} wins!")
            print("Still alive:\n")
            for hero in self.team_two.heroes:
                print(f"{hero.name}")
        else:
            print("Draw")

        print(f"{self.team_one.name}'s average kill/death rate: {team_one_stats}")
        print(f"{self.team_two.name}'s average kill/death rate: {team_two_stats}")


class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        return random.randint(self.max_damage//2, self.max_damage)

class Team(Hero):
    def __init__(self, name):
        ''' Initialize your team with its team name
        '''
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        for hero in self.heroes:
            if name == hero.name:
                self.heroes.remove(hero)

        return 0

    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        self.heroes.append(hero)

    def attack(self, other_team):
        ''' Battle each team against each other.'''
        while self.heroes_alive() and other_team.heroes_alive():
            hero1 = random.choice(self.heroes)
            hero2 = random.choice(other_team.heroes)
            hero1.fight(hero2)

    def heroes_alive(self):
        for hero in self.heroes:
            if hero.is_alive():
                return True
        return False

    def revive_heroes(self):
        ''' Reset all heroes health to starting_health'''
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def stats(self):
        '''Print team statistics'''
        kd_ratio = 0
        total = 0
        for hero in self.heroes:
            if hero.deaths == 0:
                return hero.kills
            else:
                kd_ratio = hero.kills // hero.deaths
                total += kd_ratio

        return total



if __name__ == "__main__":
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()



























