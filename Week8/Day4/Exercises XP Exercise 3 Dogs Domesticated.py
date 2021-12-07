# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 21:25:52 2021

@author: 97250
"""

# Exercise 3 : Dogs Domesticated

import Exercises_XP as module
import random

class PetDog(module.Dog):
    def __init__(self, name, age, weight, trained = False):
        super().__init__(name, age, weight)
        self.trained = trained
        
    def trained_dog(self): # nice try here! we cannot use the same name for attribute and method at the same class ... 
                           # there is no real privacy in Python :) once again - nice try
        print(self.bark())
        
        self.trained = True
        
        return True
        
    
    def play(self, *args):
        result = str(self.name) + ' ' + ' '.join(list(args))
        
        print(f"{result} - all playing together")
        
        return True
    
    def do_a_trick(self):
        
        action_list = [f"{self.name} does a barrel roll", 
                       f"{self.name} stands on his back legs",
                       f"{self.name} shakes your hand",
                       f"{self.name} plays dead"]
        
        if self.trained == True:
            print(random.choice(action_list))
        
        return True
    def info(self):
        print(f"dog name: {self.name}, age {self.age} y.o., weight {self.weight} kg, trained: {self.trained}")
    
#################################################################################


dogs_list = [PetDog('PetDog1', 12, 4), PetDog('PetDog2', 23, 3), PetDog('PetDog3', 32, 33)]

for el in dogs_list:
    el.info()
    
    el.trained_dog()
    
    el.do_a_trick()

dogs_names_list = [el.name for el in dogs_list]

new_dog = PetDog("newName", 1, 1)

new_dog.play(*dogs_names_list)

