# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 09:26:34 2021

@author: 97250
"""

import random

class Gene():
    def __init__(self, value = True):
        self.value = value
    
    def flip(self):
        self.value = not self.value
        
        return self
    
    def info(self):
        result = 1 if self.value else 0
        
        return f"{result}"

class Chromosomes(Gene):
    
    Chromosomes_lenght = 10
    
    def __init__(self):
        super().__init__()
        
        self.gene_list = [Gene(bool(random.getrandbits(1))) for i in range(Chromosomes.Chromosomes_lenght)]
    
    def flip(self):
        self.gene_list = [el.flip() for el in self.gene_list]
        
        return self

    def info(self):
        result = '-'.join([el.info() for el in self.gene_list])
        
        return f"{result}"

class DNA(Chromosomes):
    
    DNA_lenght = 10
    
    def __init__(self):
        super().__init__()
        
        self.DNA_list = [Chromosomes() for i in range(DNA.DNA_lenght)]
        
    def flip(self):
        self.DNA_list = [el.flip() for el in self.DNA_list]
            
        return self.DNA_list

    def info(self):
        result = '+++'.join([el.info() for el in self.DNA_list])
            
        print(f"DNA info: {result}")
        
        
class Organism(DNA):
    def __init__(self, enviroment_param = 1):
        
        """
        Info: an environment parameter that sets the probability for its DNA to mutate
        """
        
        super().__init__()
        
        self.enviroment_param = enviroment_param
        
    def flip(self):
        if self.enviroment_param > 0.5:
            super(DNA, self).flip()
        
        return True
            
    def change_enviroment_param(self, param):
        
        self.enviroment_param = param
        
        return True
    
    
    def check_status(self):
        
        result = False if '0' in super(DNA, self).info() else True
        
        a = '0'
        print(f"check status: {super(DNA, self).info().count(a)}, {super(DNA, self).info()}")
        
        return result
    
    def info(self):
        
        print(f"Organism info: {self.enviroment_param}")
        super(DNA, self).info()
        
        return True
        
        
        
###########################################################################################################

cr1 = Chromosomes()
cr1.info()

cr1.flip()
print("-----------------------flip Chromosomes has been called here---------------------")
cr1.info()

print("-----------------------DNA---------------------")
d1 = DNA()
d1.info()

d1.flip()
d1.info()

print("-----------------------Organizm---------------------")
o1 = Organism()
i = 0 # iterator
param_counter = 0

while i < 10:
    i += 1

    if o1.check_status():
        print("bingo!")
        break

    o1.flip()
    
    param = random.uniform(0, 1)
    
    if param > 0.5:
        param_counter += 1
        
    o1.change_enviroment_param(param)
    
print(f"totaly we did {i} iterations, while only {100*(param_counter / i)} % succseed")

o1.info()