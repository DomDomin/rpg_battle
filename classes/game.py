import random
# from classes.magic import Spell


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    YELLOW = '\033[93m'
    FAIL = '\033[31m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CYAN = '\033[96m'
    GREY = '\033[90m'
    RED_LIGHT = '\033[91m'
    MAGENTA = '\033[35m'


class Person:

    def __init__(self, name, hp, mp, atkl, atkh, crit, defense, magic, mp_regen):
        self.name = name
        self.hp = hp
        self.maxhp = hp
        self.mp = mp
        self.maxmp = mp
        self.atkl = atkl
        self.atkh = atkh
        self.crit = crit
        self.defense = defense
        self.magic = magic
        self.mp_regen = mp_regen
        self.actions = ["Attack", "Magic", "Skip turn"]

    def generate_dmg(self):
        crit_range = 100 - self.crit
        crit_roll = random.randrange(1, 100)
        if crit_roll >= crit_range:
            return (random.randrange(self.atkl, self.atkh))*1.5
        else:
            return random.randrange(self.atkl, self.atkh)
    
    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp
    
    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp
    
    def get_hp(self):
        return self.hp
    
    def get_maxhp(self):
        return self.maxhp
    
    def get_mp(self):
        return self.mp
    
    def get_maxmp(self):
        return self.maxmp
    
    def reduce_mp(self, i):
        self.mp -= self.magic[i].cost
        if self.mp < 0:
            self.mp = 0
        return self.mp
    
    def regen_mp(self):
        self.mp += self.mp_regen
        if self.mp > self.maxmp:
            self.mp = self.maxmp
        return self.mp
    
    def choose_action(self):
        i = 1
        print(bcolors.CYAN + bcolors.BOLD, "Actions:", bcolors.ENDC)
        for item in self.actions:
            print(str(i) + ".", item)
            i+=1
    
    def choose_magic(self):
        i = 1
        print(bcolors.MAGENTA + bcolors.BOLD, "\nMagic:", bcolors.ENDC)
        for spell in self.magic:
            print(str(i) + ".", spell.name, "(mp cost:", str(spell.cost) + ", dmg:", str(spell.dmg) + ")")
            i+=1
