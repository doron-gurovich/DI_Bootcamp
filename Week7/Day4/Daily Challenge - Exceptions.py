# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 11:34:00 2021

@author: 97250
"""

def simple_calc_div(num1 = 5, num2 = 0):
    
    """
    Info: Write a function to compute 5/0 and use try/except to catch the exceptions.
    """
    
    try:
        return num1/num2
    except ZeroDivisionError:
        return "integer division by zero"

print(simple_calc_div(10, 2), "\n", simple_calc_div())