import random

class Spell:

    def __init__(self, name, cost, dmg, type, element):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type
        self.element = element

    def generate_spell_dmg(self):
        spell_dmgl = self.dmg - 5
        spell_dmgh = self.dmg + 10
        return random.randrange(spell_dmgl, spell_dmgh)