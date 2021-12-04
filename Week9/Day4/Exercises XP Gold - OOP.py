# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 17:52:37 2021

@author: 97250
"""

class Door():
    
    objs = 1
    
    def __init__(self, isLocked, *next_door):
        self.id_door = Door.objs
        Door.objs += 1

        self.isLocked = isLocked
        self.next_door = next_door

    
    def get_door_by_int(self, num):
        
        pass
        
    def can_go_to (self, other):
        
#        for i in range(1, Door.objs):
            
         
        
        return True


d1 = Door(True, *[2, 3, 8])
d2 = Door(False, *[1, 5, 6, 7])
d3 = Door(False, *[1, 8, 15])
d4 = Door(True, *[4, 9, 10, 12, 13, 14])
d5 = Door(False, *[2, 16])
d6 = Door(False, *[2, 16])
d7 = Door(False, *[2, 16])
d8 = Door(True, *[3, 19])
d9 = Door(True, *[4, 11])
d10 = Door(False, *[4, 11])
d11 = Door(True, *[9, 10, 12])
d12 = Door(True, *[4, 11, 18])
d13 = Door(False, *[4, 18])
d14 = Door(False, *[4, 18])
d15 = Door(True, *[3, 19])
d16 = Door(False, *[5, 6, 7, 17])
d17 = Door(False, *[16, 18, 19])
d18 = Door(True, *[12, 13, 14])
d19 = Door(True, *[8, 15, 17])