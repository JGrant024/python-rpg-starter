# """
# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

# """

# def main():
#     hero_health = 10
#     hero_power = 5
#     goblin_health = 6
#     goblin_power = 2

#     while goblin_health > 0 and hero_health > 0:
#         print("You have %d health and %d power." % (hero_health, hero_power))
#         print("The goblin has %d health and %d power." % (goblin_health, goblin_power))
#         print()
#         print("What do you want to do?")
#         print("1. fight goblin")
#         print("2. do nothing")
#         print("3. flee")
#         print("> ",)
#         user_input = input()
#         if user_input == "1":
#             # Hero attacks goblin
#             goblin_health -= hero_power
#             print("You do %d damage to the goblin." % hero_ cpower)
#             if goblin_health <= 0:
#                 print("The goblin is dead.")
#         elif user_input == "2":
#             pass
#         elif user_input == "3":
#             print("Goodbye.")
#             break
#         else:
#             print("Invalid input %r" % user_input)

#         if goblin_health > 0:
#             # Goblin attacks hero
#             hero_health -= goblin_power
#             print("The goblin does %d damage to you." % goblin_power)
#             if hero_health <= 0:
#                 print("You are dead.")

# main()

import random

class Hero:
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        damage = random.randint(1, self.power)
        enemy.health -= damage

    def print_status(self, enemy):
      print(self.health, enemy.health)
        
class Goblin(Hero):
    def __init__(self, name):
     super().__init__(health=6, power=2, name=name)

hero = Hero(name = "Hero", health=10, power=5)
goblin = Goblin(name = "Goblin")


while goblin.alive() and hero.alive():  
    print("What do you want to do?")
    print("1. fight goblin")
    print("2. do nothing")
    print("3. flee")
    user_input = input()

    if user_input == "1": 
        hero.attack(goblin)
        hero.print_status(goblin)
        print("You do %d damage to the goblin." % (hero.power))
    elif user_input == "2": 
        goblin.attack(hero)
    elif user_input == "3": 
        print("If you're scared just say that! See ya! ")
        break
    if not goblin.alive(): 
        goblin.print_status(goblin)
        print("Victory is mine Goblin ")
        break

    if not hero.alive():
        print("You are dead.")
        break

    
    
    
    
    
  


