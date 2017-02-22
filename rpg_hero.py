import time

class Hero(object):
    def __init__(self):
        self.name = "Sean"
        self.health = 10
        self.power = 5
    def is_alive(self):
        return self.health > 0;
        # if self.health > 0:
        #     return true
        # else:
        #     return false
    def attack(self, enemy):
        print "%s attacks %s" % (self.name, enemy.name)
        enemy.take_damage(self.power)
        time.sleep(1.5)
        print "%s has done %d damage to %s" % (self.name, self.power, enemy.name)
        print "         __                                     __"
        print "  ____  / /_     ____ ___  __  __   ____  _____/ /_"
        print " / __ \/ __ \   / __ `__ \/ / / /  /_  / / ___/ __ \ "
        print "/ /_/ / / / /  / / / / / / /_/ /    / /_(__  ) / / /"
        print "\____/_/ /_/  /_/ /_/ /_/\__, /    /___/____/_/ /_/"
        print "                           /_/"
        
        time.sleep(1)



class Fellowship_Of_The_Ring(object):
    def __init__(self,name,race,health,speed,strength,weapon,weapon_power):
        self.name = name
        self.race = race
        self.health = health
        self.speed = speed
        self.strength = strength
        self.weapon = weapon
        self.weapon_power = weapon_power
    def help_frodo(self):
        print "You can do it Frodo. Trust " + self.name + "!"

Aragorn = Fellowship_Of_The_Ring("Aragorn","Human",50,8,9,"Anduril","8")
# print Aragorn
# print vars(Aragorn)

Gimli = Fellowship_Of_The_Ring("Gimli","Dwarf",50,5,10,"Battle Axe","7")

Frodo = Fellowship_Of_The_Ring("Frodo","Hobbit",50,7,6,"Sting","6")

Gandalf = Fellowship_Of_The_Ring("Gandalf","Wizard",50,8,10,"Glamdring & Wizard Staff","9")

Samwise_Gamgee = Fellowship_Of_The_Ring("Samwise","Hobbit",50,5,10,"Barrow Blade","5")
