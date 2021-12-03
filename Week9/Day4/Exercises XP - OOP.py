# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 17:52:11 2021

@author: 97250
"""


class Human():
    
    def __init__(self, name, age, living_place = None):
        self.name = name
        self.age = age
        self.living_place = living_place
    
    def move(self, building):
        self.living_place = building
        
        building.inhabitants.append(self)
        
        return True # and as always we could prevent incorrect type by checking it
    
class Building():
    
    def __init__(self, address):
        self.address = address
        self.inhabitants = [] # List of Human objs - Default is empty


class City():
    
    def __init__(self, name):
        self.name = name
        self.buildings = []
    
    def construct(self, address):
        
        self.buildings.append(Building(address))
        
        return True
    
    def info(self, address):
        
        num_of_buildings = len(self.buildings)
        mean_age_of_citizens = 0
        
        temp = []
        
        for el in self.buildings:
            for i in el.inhabitants:
                temp.append(i.age)
        
        mean_age_of_citizens = sum(temp) / len(temp)
        
        print(f"""
              city: {self.name}
              number of buildings: {num_of_buildings}
              mean age of citizens: {mean_age_of_citizens}
              """)
      
    def address_to_class(self, address_to_check):
            
        for el in self.buildings:
            if el.address == address_to_check:
                return el


h1 = Human("name1", 10)
h2 = Human("name2", 20)
h3 = Human("name3", 30)
h4 = Human("name4", 40)
h5 = Human("name5", 50)

c1 = City("c1")

c1.construct("b1-1")

h1.move(c1.address_to_class("b1-1"))
h2.move(c1.address_to_class("b1-1"))
h3.move(c1.address_to_class("b1-1"))
h4.move(c1.address_to_class("b1-1"))
h5.move(c1.address_to_class("b1-1"))

c1.info("b1-1")