class Goblin(object):
    def __init__(self):
        self.name = "Gob"
        self.health = 6
        self.power = 2
    def is_alive(self):
        return self.health > 0;
        # if self.health > 0:
        #     return true
        # else:
        #     return false
    def take_damage(self, points_of_damage):
        self.health -= points_of_damage;
    def attack(self, hero):
        print "%s attacks %s" % (self.name, hero.name)
        hero.take_damage(self.power)



class Orc(object):
    def __init__(self,name,health,race,speed,strength,weapon,weapon_power):
        self.name = name
        self.race = race
        self.health = health
        self.speed = speed
        self.strength = strength
        self.weapon = weapon
        self.weapon_power = weapon_power

Orc_Grunt = Orc("Zok","Orc",5,2,2,"Rusty Dagger","2")
