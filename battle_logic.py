import characters
import random

"""
The "Run Game" function
Print Welcome message
Fight enemy 1
Fight enemy 2
Fight enemy 3
Print victory message
"""

def run_game():
    welcome()
    battle_phase(characters.hero_goku, characters.enemy_frieza)
    # battle_phase(characters.hero_goku, characters.enemy_cell)
    # battle_phase(characters.hero_goku, characters.enemy_kid_buu)

def welcome():
    print("Welcome to DragonBall RPG")
    print(f"{characters.hero_goku['name']} is the hero!")
    print("He needs to defeat")
    print(characters.enemy_frieza['name'])
    print(characters.enemy_cell['name'])
    print(f"and {characters.enemy_kid_buu['name']}!")

def battle_phase(hero, enemy):
    print(f"{hero['name']} enters into battle with {enemy['name']}")
    while hero['health'] > 0 and enemy['health'] > 0:
        random_attack = random.choice(hero['attacks'])
        print(f"{hero['name']} attacks {enemy['name']} using {random_attack[0]} for {random_attack[1]} damage")
        enemy['health'] -= random_attack[1]
        print(f"{enemy['name']} now has {enemy['health']} health.")
        if enemy['health'] > 0:
            random_attack = random.choice(enemy['attacks'])
            print(f"{enemy['name']} attacks {hero['name']} using {random_attack[0]} for {random_attack[1]} damage")
            hero['health'] -= random_attack[1]
            print(f"{hero['name']} now has {hero['health']} health.")