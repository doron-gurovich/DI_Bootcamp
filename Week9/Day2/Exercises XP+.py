# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 20:30:54 2021

@author: 97250
"""

# Exercise 1 : Family

class Family:
    def __init__(self, last_name, *args):
        
        self.last_name = last_name
        
        self.members = []
        
        input_family = list(args)
        for el in input_family:
            if type(el) == dict:
                self.members.append(dict(el.items()))

    def born(self, **kvargs):
        
        self.members.append(dict(kvargs))
        print(f"congrats w/ newborn! {self.members[-1]}")
    
    def is_18(self, name):
        
        result = False
        
        for el in self.members:
            if el['name'] == name and el['age'] >= 18:
                result = True
        
        return result
    
    def print_all_members(self):
        
        for el in self.members:
            print(el)

list_input = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
]

k1 = {'name':'Michael++','age':0,'gender':'Male','is_child':True}

QQQ = Family("QQQ family", *list_input)

# QQQ.print_all_members()

QQQ.born(**k1)
QQQ.print_all_members()

print(QQQ.is_18('Michael++'))


# Exercise 2 : TheIncredibles Family

class TheIncredibles(Family):
    
    def __init__(self, power, incredible_name, last_name, *members):
        super().__init__(self, last_name, *members)
        
        self.power = power
        self.incredible_name = incredible_name
    
    def use_power(self):
        
        """
        Info: Add a method called use_power, 
        this method should print the power of a member if they are over 18 years old. 
        If not raise an exception (look up exceptions) which stated they are not over 18 years old
        """
        
        pass
    
    def incredible_presentation(self):
        
        """
        Info: Add a method called incredible_presentation which presents the family members 
        with their incredible names and powers.
        """
        
        pass
    
# https://en.wikipedia.org/wiki/List_of_The_Incredibles_characters

# bob_list = 
Bob_Parr = TheIncredibles("strength", "Mr. Incredible", "The Parr Family", *[{'name': "Bob Parr", 'age': 38, 'gender': "Male",'is_child':False}])
