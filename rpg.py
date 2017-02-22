from rpg_hero import Fellowship_Of_The_Ring, Hero
from rpg_monsters import Orc, Goblin

hero = Hero();
enemies = [Goblin()];

for enemy in enemies:
    print vars(enemy)
    while hero.is_alive() and enemy.is_alive() > 0:
        print "What will you do?"
        print "1. Fight %s" % enemy.name
        print "2. Run away"
        print "> ",
        input = int(raw_input());
        if input == 1:
            # enemy.health -= hero.power;
            hero.attack(enemy);
        elif input == 2:
            hero.health -= enemy.power
        else:
            print "You cannot flee, You are surrounded %r" % input
        if enemy.is_alive:
            # hero.health -= enemy.power;
            enemy.attack
    if hero.is_alive > 0:
        print "You won! the %s is defeated" % (enemy.name)
    else:
        print "You were beaten by the %s" % (enemy.name)
