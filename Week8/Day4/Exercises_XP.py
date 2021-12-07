# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 21:00:49 2021

@author: 97250
"""


# Exercise 1 : Pets
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Another_Cat_Bread(Cat):
    pass

c1 = Cat("cat1", 12)
c2 = Cat("cat2", 21)

my_cats = [c1, c2]

my_pets = [Pets(c1), Pets(c2)]

for el in my_cats:
    print(el.walk())
    
# Exercise 2 : Dogs

class Dog():
    
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        
    def bark(self):
        return f"{self.name} is barking.\n"
    
    def run_speed(self):
        return self.weight / (10*self.age )
    
    def fight(self, other):
        result = self.name if self.run_speed() * self.weight > other.run_speed() * other.weight else other.name
        
        return f"{result} won the fight.\n"

d1 = Dog("dog1", 12, 23)
d2 = Dog("dog2", 23, 34)
d3 = Dog("dog3", 12, 34)

print( d1.bark(), d2.bark(), d3.bark())
print( d1.run_speed(), d2.run_speed(), d3.run_speed())

print(d1.fight(d2), d2.fight(d3), d1.fight(d3))


