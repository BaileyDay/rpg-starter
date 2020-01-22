import random
import inspect

# Initilization of the main parent character class.

class Character():
    def __init__(self):
        self.health = random.randint(15, 25)
        self.power = round(self.health/random.randint(2,3))

    def alive(self):
        if self.health > 0:
            return True
        else: 
            return False

    def attack(self, goblin):
        goblin.health -= self.power

    
# The main while loop for the battle
    
    def choose_action(self):
        while gus.alive() == True and rus.alive() == True:
            
            rus.display_menu()
            user_input = input()
            if user_input == "1":
                chance = random.randint(0,4)
                shadow_chance = random.randint(0,9)
                if inspect.isclass(Shadow):
                    if shadow_chance == 1:
                        gus.attack(rus)
                    else:
                        print("The enemys attack has missed!")
                        rus.attack(gus)
                elif chance == 1:
                    print("You got a critical hit!")
                    rus.attack(gus)
                    rus.attack(gus)
                    gus.attack(rus)
                elif chance == 2:
                    print("Your attack missed!")
                    gus.attack(rus)
                elif chance == 3:
                    print("The enemys attack missed!")
                    rus.attack(gus)
                else:
                    rus.attack(gus)
                    gus.attack(rus)
                if gus.health <= 0:
                    print("You have slayed the beast!")
                if rus.health <= 0:
                    print("You have been slain. =(")
            elif user_input == "2":
                print("You ran like a coward.")
                gus.attack(rus)
                if rus.health <= 0:
                    print("You have been slain. =(")
                break
            elif user_input == "3":
                gus.attack(rus)
                gus.attack(rus)
                gus.attack(rus)
                if rus.health <= 0:
                    print("You have been slain. =(")
                
            else:
                print("Invalid input. Try again")

            if inspect.isclass(Medic) == True:
                if chance == 1:
                    self.health += 2
                    print("Passive healing activated")
            
# Display menu to choose your options.

    def display_menu(self):
        print("You have {} health and {} power.".format(rus.health, rus.power))
        print("The goblin has {} health and {} power.".format(gus.health, gus.power))

        print("Choose your option: ")
        print("1 -- Fight the goblin")
        print("2 -- Run from the goblin")
        print("3 -- Do nothing")

# Child classes available for battle. 

class Hero(Character):
    def attack(self, goblin):
        goblin.health -= self.power

class Goblin(Character):
    def goblin_attack(self, hero):
        hero.health -= self.power

class Medic(Character):
    pass

class Shadow(Character):
    def __init__ (self):
        self.health = 1
        self.power = 3

# The character selection options

def choose_character():
    user_input = input("Choose your character! \n 1 - Hero \n 2 - Medic \n 3 - Shadow \n 4 - Zombie \n")
    if user_input == "1":
        rus = Hero()
    elif user_input == "2":
        rus = Medic()
    elif user_input == "3":
        rus = Shadow()
    elif user_input == "4":
        rus = Zombie()
    else:
        print("Incorrect character selection! Goodbye!")
        exit()
    return rus

gus = Goblin()

rus = choose_character()         

rus.choose_action()




