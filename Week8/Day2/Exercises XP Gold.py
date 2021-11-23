# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 10:49:19 2021

@author: 97250
"""

#Exercise 1 : Geometry

import math
import random

class Circle:
    def __init__(self, radius = 1.0):
        self.radius = radius
        
    def perimeter(self):
        return 2*math.pi*self.radius
    
    def area(self):
        return math.pi*self.radius**2
    
    def definition_of_the_circle(self):
        print("A circle is a shape consisting of all points in a plane that are at a given distance from a given point, the centre; equivalently it is the curve traced out by a point that moves in a plane so that its distance from a given point is constant.")
        
        return True

c1 = Circle()
c2 = Circle(10)

print(f"for c1 we have: radius ({c1.radius}), perimeter ({c1.perimeter()}) and area ({c1.area()})")
print(f"for c1 we have: radius ({c2.radius}), perimeter ({c2.perimeter()}) and area ({c2.area()})")

c1.definition_of_the_circle()

# Exercise 2 : Custom List Class

class MyList:
    def __init__(self, *list_of_letters):
        self.list_of_letters = list(list_of_letters).copy()
    
    def self_return(self):
        return self.list_of_letters
    
    def self_return_sorted(self):
        
        result = list(self.list_of_letters).copy()
        
        result.sort()
        
        return result
    
    def random_list(self):
        
        result = [i*random.randint(0, 100) for i in range(0, len(list(self.list_of_letters)))]
        
        return result

i1 = ['q', 'w', 'e', 'a', 'c', 'b']
    
l1 = MyList(i1)

l2 = l1.self_return()
l3 = l1.self_return_sorted()

l4 = l1.random_list()