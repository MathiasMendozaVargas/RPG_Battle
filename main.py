from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item


# Create Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 15, 150, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 12, 120, "black")

# Create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# Create Games Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals for 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals for 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP for one party member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores HP/MP for all party members", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [potion, hipotion, superpotion, elixer, hielixer, grenade]

# Instantiate People
player = Person(360, 75, 60, 34, player_spells, player_items)
enemy = Person(1230, 65, 45, 25, [], [])

running = True

print(bcolors.FAIL + bcolors.BOLD + "****** AN ENEMY ATTACKS! ******" + bcolors.ENDC)

while running:
    player.choose_action()
    choose = input("Choose action: ")
    index = int(choose) - 1

    if index == 0:
        player_dmg = player.generate_dmg()
        enemy.take_damage(player_dmg)
        print("You attack for", player_dmg, "points of damage. Enemy HP is:", enemy.get_hp())
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic: ")) - 1

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if magic_choice == -1:
            continue

        if spell.cost > current_mp:
            print(bcolors.FAIL + "Not Enough MP..." + bcolors.ENDC)
            continue
        player.reduce_mp(spell.cost)

        if spell.type == "white":
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + bcolors.ENDC)
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage..." + bcolors.ENDC)
        player_mp = player.get_mp()
        if player_mp < 0:
            player_mp = 0
        enemy.take_damage(magic_dmg)
    elif index == 2:
        player.choose_item()
        item_choice = int(input("Choose item: ")) -1

        if item_choice == -1:
            continue

        item = player.item[item_choice]
        if item.type == "potion":
            player.heal(item.prop)
            print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + bcolors.ENDC)
        elif item.type == "elixer":
            player.hp = player.maxhp
            player.mp = player.maxmp
            print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + bcolors.ENDC)
        elif item.type == "attack":
            enemy.take_damage(item.prop)
            print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage" + bcolors.ENDC)

    enemy_dmg = enemy.generate_dmg()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "Your current HP is", player.get_hp())

    print("=========================")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_maxhp()) + bcolors.ENDC)
    print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_maxhp()) + bcolors.ENDC)
    print("Your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_maxmp()) + bcolors.ENDC)

    if player.get_hp() == 0:
        print(bcolors.FAIL + bcolors.BOLD + "You Lost..." + bcolors.ENDC)
        running = False
    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + bcolors.BOLD + "You Win!" + bcolors.ENDC)
        running = False




