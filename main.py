import random
import time
from classes.game import Person, bcolors
from classes.magic import Spell


print("\n" + bcolors.BOLD, bcolors.UNDERLINE, "FIRST RPG BATTLE", bcolors.ENDC, "\n")

#Magic spells
# magic = [{"name": "Fireball", "cost": 8, "dmg": 40, "type": bcolors.RED_LIGHT + "fire" + bcolors.ENDC},
#          {"name": "Frozen spike", "cost": 6, "dmg": 30, "type": bcolors.OKBLUE + "cold" + bcolors.ENDC},
#          {"name": "Spark", "cost": 4, "dmg": 20, "type": bcolors.YELLOW + "lightning" + bcolors.ENDC}]

#Spell classes
fireball = Spell("Fireball", 8, 40, "offensive", bcolors.RED_LIGHT + "fire" + bcolors.ENDC)
frozen_spike = Spell("Frozen spike", 6, 30, "offensive", bcolors.OKBLUE + "cold" + bcolors.ENDC)
spark = Spell("Spark", 4, 20, "offensive", bcolors.YELLOW + "lightning" + bcolors.ENDC)
heal = Spell("Heal", 10, 100, "healing", bcolors.OKGREEN + "divine" + bcolors.ENDC)

spells = [fireball, frozen_spike, spark, heal]

#Heroes classes
hero1 = Person("Domin", 200, 30, 20, 35, 15, 15, spells, 3)

heroes = [hero1]

#Enemy classes
enemy1 = Person("Ogre", 150, 20, 10, 15, 5, 5, spells, 1)
enemy2 = Person("Imp", 50, 40, 8, 13, 7, 4, spells, 2)
enemy3 = Person("Skeleton warrior", 80, 20, 20, 28, 10, 8, spells, 1)

enemies = [enemy1, enemy2, enemy3]

running = True

print("You slowly enter the dungeon that you've finally found. Directions given by the archmage weren't really specific, but your years of adventuring paid off, by making it easier to discover the entrance. Walking slowly, you notice thin rope just a couple centimeters above the ground, coming out from one corridor wall and going to the opposite wall. 'Such an obvious trap' - you smile to yourself while disarming it quickly. Peaking around the corner you see an enemy. Since there is no other way to proceed, you'll have to fight.")
time.sleep(7)
roll_enemy = random.randrange(0, len(enemies))
encountered_enemy = enemies[roll_enemy]

print("\nIt's time to face the", encountered_enemy.name + ".\n")
time.sleep(2)
print(bcolors.YELLOW + bcolors.BOLD + "Let the battle begin!" + bcolors.ENDC, "\n")
time.sleep(1)

def fight():
    running = True
    while running == True:

    #DISPLAYING HERO NAME, HP, MP
        print(bcolors.OKGREEN + bcolors.BOLD + "Player Team:" + bcolors.ENDC)
        for hero in heroes:
            print(bcolors.OKGREEN + hero.name + bcolors.ENDC, "    HP:", hero.get_hp(), "/", hero.get_maxhp(), "    MP:", hero.get_mp(), "/", hero.get_maxmp(), "\n")

    #DISPLAYING ENCOUNTERED ENEMY NAME, HP, MP
        print(bcolors.FAIL + bcolors.BOLD + "Enemy Team:" + bcolors.ENDC)
        print(bcolors.FAIL + bcolors.BOLD + encountered_enemy.name + bcolors.ENDC, "    HP:", encountered_enemy.get_hp(), "/", encountered_enemy.get_maxhp(), "    MP:", encountered_enemy.get_mp(), "/", encountered_enemy.get_maxmp(), "\n")

    #HERO ATTACKS
        if hero1.hp > 0 and encountered_enemy.hp > 0:
            hero_turn = True
        else:
            hero_turn = False
        while hero_turn == True:
        
            hero1.choose_action()
            hero1_action_choice = input("\nChoose action: ")
            if hero1_action_choice == "1":
                dmg = hero1.generate_dmg()
                encountered_enemy.take_damage(dmg)
                if encountered_enemy.hp > 0:
                    print("\nYou hit", encountered_enemy.name, "for", dmg, "points of damage. Enemy is left with", encountered_enemy.get_hp(), "hp.")
                    hero_turn = False
                else:
                    print("\nYou hit", encountered_enemy.name, "for", dmg, "points of damage. Enemy is dead.")
                    break
            elif hero1_action_choice == "2":
                hero1.choose_magic()
                go_back_number = len(hero1.magic) + 1
                print(str(go_back_number) + ". Back")
                magic_choice = int(input("\nChoose spell or go back: ")) - 1
                hero1_spell = hero1.magic[magic_choice]
                if magic_choice + 1 == go_back_number:
                    continue
                else:
                    if hero1.mp >= hero1_spell.cost:
                        hero1.reduce_mp(magic_choice)
                        if hero1_spell.type == "offensive":
                            magic_dmg = hero1_spell.generate_spell_dmg()
                            encountered_enemy.take_damage(magic_dmg)
                            if encountered_enemy.hp > 0:
                                print("\nYou hit", encountered_enemy.name, "for", magic_dmg, "points of", hero1_spell.element, "damage. Enemy is left with", encountered_enemy.get_hp(), "hp.")
                                hero_turn = False
                            else:
                                print("\nYou hit", encountered_enemy.name, "for", magic_dmg, "points of", hero1_spell.element, "damage. Enemy is dead.")
                                break
                        elif hero1_spell.type == "healing":
                            heal_amount = hero1_spell.generate_spell_dmg()
                            hero1.heal(heal_amount)
                            print("\nYou heal for", bcolors.OKGREEN + str(heal_amount) + bcolors.ENDC, "HP points. Current HP:", str(hero1.get_hp()) + ".")
                            hero_turn = False
                        else:
                            print("Something went wrong. Choose again your action.")
                            continue
                    else:
                        print("\nNot enough MP.")
                        continue    
            elif hero1_action_choice == "3":
                break
            else:
                print("\nType '1' or '2' and hit enter")
                continue
       
        time.sleep(1)

    #ENEMY ATTACKS
        if encountered_enemy.hp > 0 and hero1.hp > 0:
            enemy_turn = True
        else:
            enemy_turn = False
        while enemy_turn == True:
            enemy_action_choice = random.randrange(1, 3)
            if enemy_action_choice == 1:
                dmg = encountered_enemy.generate_dmg()
                hero1.take_damage(dmg)
                if hero1.hp > 0:
                    print("\nEnemy hits you for", dmg, "points of damage. You are left with", hero1.get_hp(), "hp.\n")
                    enemy_turn = False
                else:
                    print("\nEnemy hits you for", dmg, "points of damage.", bcolors.FAIL + "YOU ARE DEAD!" + bcolors.ENDC)
                    enemy_turn = False
            elif enemy_action_choice == 2:
                enemy_magic_choice = int(random.randrange(1, (len(spells) + 1))) -1
                encountered_enemy_spell = encountered_enemy.magic[enemy_magic_choice]
                if encountered_enemy.mp >= encountered_enemy_spell.cost:
                    encountered_enemy.reduce_mp(enemy_magic_choice)
                    if encountered_enemy_spell.type == "offensive":
                        enemy_magic_dmg = encountered_enemy_spell.generate_spell_dmg()
                        hero1.take_damage(enemy_magic_dmg)
                        if hero1.hp > 0:
                            print("\nEnemy hits you with", encountered_enemy_spell.name, "for", enemy_magic_dmg, encountered_enemy_spell.element, "damage. You are left with", hero1.get_hp(), "hp.\n")
                            enemy_turn = False
                        else:
                            print("\nEnemy hits you with", encountered_enemy_spell.name, "for", enemy_magic_dmg, encountered_enemy_spell.element, "damage.", bcolors.FAIL + "YOU ARE DEAD!" + bcolors.ENDC)
                            enemy_turn = False
                    elif encountered_enemy_spell.type == "healing":
                        heal_amount = encountered_enemy_spell.generate_spell_dmg()
                        encountered_enemy.heal(heal_amount)
                        print("\nEnemy heals for", bcolors.OKGREEN + str(heal_amount) + bcolors.ENDC, "HP points.")
                        enemy_turn = False
                    else:
                        print("\nEnemy failed to cast the spell.")
                        continue
                else:
                    continue
            else:
                print("\nEnemy failed to attack.\n")
                continue
        
        if hero1.hp > 0:
            hero1.regen_mp()
        if encountered_enemy.hp > 0:
            encountered_enemy.regen_mp()
        if encountered_enemy.hp == 0 or hero1.hp == 0:
            running = False
        else:
            time.sleep(1)
            continue

fight()


if encountered_enemy.hp > 0 and hero1.hp == 0:
    print("\n" + encountered_enemy.name, "has defeated you. You have failed your quest.")
    exit()
elif hero1.hp > 0 and encountered_enemy.hp == 0:
    enemies.pop(roll_enemy)
    time.sleep(2)
    print("\nYou defeated", encountered_enemy.name + ". You can explore further parts of the dungeon now.\n")
    time.sleep(2)
    print("Exploring this dungeon doesn't feel any different, from the other dungeons you've been to. With confidence, but caution at the same time, you proceed further. As you go, you light up the torches on the wall, so you can see anything in this dark corridor. Suddenly, while taking care of another torch, you notice another foul creature coming your way.")
    roll_enemy = random.randrange(0, len(enemies))
    encountered_enemy = enemies[roll_enemy]
    time.sleep(2)
    print("\nYou recognize the shape of the monster as it slowly emerges from the shadows. It's", encountered_enemy.name + ".\n")
    fight()
else:
    print("What have happend ? :o")
    exit()

