import characters
import random
from slow_print_text import slow_print
from colorama import Fore

def run_game():
    welcome()
    battle_phase(characters.hero_goku, characters.enemy_frieza)
    battle_winner(characters.hero_goku, characters.enemy_frieza)
    battle_phase(characters.hero_goku, characters.enemy_cell)
    battle_winner(characters.hero_goku, characters.enemy_cell)
    battle_phase(characters.hero_goku, characters.enemy_kid_buu)
    battle_winner(characters.hero_goku, characters.enemy_kid_buu)

def welcome():
    slow_print(f"{Fore.MAGENTA}Welcome to DragonBall RPG")
    slow_print(f"{characters.hero_goku['name']} is the hero!")
    slow_print("He needs to defeat")
    slow_print(characters.enemy_frieza['name'])
    slow_print(characters.enemy_cell['name'])
    slow_print(f"and {characters.enemy_kid_buu['name']}!")

def battle_phase(hero, enemy):
    slow_print(f"{Fore.RESET}{hero['name']} enters into battle with {enemy['name']}")
    while hero['health'] > 0 and enemy['health'] > 0:
        random_attack = random.choice(hero['attacks'])
        slow_print(f"{Fore.BLUE}{hero['name']} attacks {enemy['name']} using {random_attack[0]} for {random_attack[1]} damage")
        enemy['health'] -= random_attack[1]
        slow_print(f"{Fore.RESET}{enemy['name']} now has {enemy['health']} health.")
        if enemy['health'] > 0:
            random_attack = random.choice(enemy['attacks'])
            slow_print(f"{Fore.RED}{enemy['name']} attacks {hero['name']} using {random_attack[0]} for {random_attack[1]} damage")
            hero['health'] -= random_attack[1]
            slow_print(f"{Fore.RESET}{hero['name']} now has {hero['health']} health.")

def battle_winner(hero, enemy):
    if hero['health'] > 0 and hero['level'] == 3:
        slow_print(f"Congrats! {hero['name']} has defeated all three enemies and wins!")
    elif hero['health'] > 0:
        slow_print(f"{Fore.LIGHTMAGENTA_EX}{hero['name']} defeated {enemy['name']}")
        slow_print("and took a Senzu Bean to restore his health in preparation for his next battle!")
        hero_prepares(hero)
        hero_loots(hero, enemy)
    else:
        slow_print(f"Game Over! {enemy['name']} defeated you.")

def hero_prepares(hero):
    hero['health'] = 150
    hero['level'] += 1
    slow_print(f"Level up! {hero['name']} is now level {hero['level']}.")
    new_attacks_list = [("Energy Wave", 25), ("Explosive Wave", 50)]
    if new_attacks_list[0]:
        new_attack = new_attacks_list.pop(0)
        slow_print(f"{hero['name']} gets a new attack {new_attack[0]} that does {new_attack[1]} damage.")
        hero['attacks'] = list(hero['attacks'])
        hero['attacks'].append(new_attack)
        hero['attacks'] = tuple(hero['attacks'])

def hero_loots(hero, enemy):
    for item in enemy['equipment']:
        slow_print(f"{Fore.RESET}{hero['name']} loots {item}")
    hero['equipment'].update(enemy['equipment'])
    