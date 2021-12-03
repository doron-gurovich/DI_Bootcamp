# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:33:22 2021

@author: 97250
"""

class Character:
    
    def __init__(self, name, life = 20, attack = 10):
        self.name = name
        self.life = life
        self.attack = attack
        
    
    def basic_attack(self, other):
        
        if type(other) == Character:
            other.life -= self.attack
        else:
            raise TypeError("Only Character available here.")
            return False
        
        return True
    
    def whatsup(self):
        print(f"character status: \nName: {self.name} \nLife: {self.life} \nAttack: {self.attack} \n")
        
        return True
    
class Druid(Character):
    def __init__(self, name, life, attack):
        super(Druid, self).__init__(name, life, attack)
    
    def meditate(self):
        
        self.life += 10
        self.attack -= 2
        
        return True
    
    def animal_help(self):
        
        self.attack += 5
        
        return True
    
    def fight(self, other):
        
        if type(other) == Character:
            other.life -= 0.75*self.life + 0.75*self.attack
        else:
            raise TypeError("Only Character available here.")
            return False
        
        return True


class Warrior(Character):
    def __init__(self, name, life, attack):
        super(Warrior, self).__init__(name, life, attack)
    
    def brawl(self, other):
        
        if type(other) == Character:
            other.life -= 2*self.attack
            self.life += 0.5*self.attack
        else:
            raise TypeError("Only Character available here.")
            return False
        
        return True

    def train(self):
        
        self.life += 2
        self.attack += 2
        
        return True

    def roar(self, other):
        
        if type(other) == Character:
            other.attack -= 3
        else:
            raise TypeError("Only Character available here.")
            return False
        
        return True


class Mage(Character):
    pass

h1 = Character("h1")
h2 = Character("h2", 30, 5)
h3 = Character("h3", 30, 1)

h1.whatsup()
h2.whatsup()
h3.whatsup()

print("============================h1 --> h3============================")
h1.basic_attack(h3)

h1.whatsup()
h2.whatsup()
h3.whatsup()
