# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 20:31:20 2021

@author: 97250
"""

import math
import matplotlib.pyplot as plt

class Circle:
    
    """
    Info: The goal is to create a class that represents a simple circle.
    A Circle can be defined by either specifying the radius or the diameter.
    The user can query the circle for either its radius or diameter.

    Other abilities of a Circle instance:

        Compute the circle’s area
        Print the circle and get something nice
        Be able to add two circles together
        Be able to compare two circles to see which is bigger
        Be able to compare two circles and see if there are equal
        Be able to put them in a list and sort them
    """
    
    def __init__(self, radius = .2):
        self.radius = radius
        self.diameter = 2*radius
        
    def area(self):
        return self.radius**2*math.pi
    
    def perimeter(self):
        return 2*self.radius*math.pi
    
    def print_circle(self):
        
        figure, axes = plt.subplots()
        Drawing_colored_circle = plt.Circle(( 1.5*self.radius , 1.5*self.radius ), 
                                            self.radius,
                                            fill = False )
 
        axes.set_aspect( 1 )
        axes.add_artist( Drawing_colored_circle )
        plt.title( 'the Circle' )
        plt.show()
   
    def  __add__(self, other):
       
       result = self.radius + other.radius
       
       return Circle(result)
   
    
    def __lt__(self, other):
        
        result = False
        
        if self.radius < other.radius:
            result = True
        
        return result
    
    def __gt__(self, other):
        
        result = False
        
        if self.radius > other.radius:
            result = True
        
        return result
    
    def __eq__(self, circle):
        result = False
        
        if self.radius == circle.radius:
            result = True
            
        return result
    
    def sort(self, *args):
        
        result = []
        input_list = list(args)
        
        input_list_raduis = [c.radius for c in input_list]
        input_list_raduis.sort()
        
        
        for r in input_list_raduis:
            for c in input_list:
                if c.radius == r:
                    result.append(c)
        
        return result

c1 = Circle()
c1.print_circle()

c2 = Circle(2)
c3 = Circle(3)

l_circle = [c3, c1, c2]

l_circle_sorted = c1.sort(*l_circle)