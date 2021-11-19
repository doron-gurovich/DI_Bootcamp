# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 11:32:38 2021

@author: 97250
"""

import random
import functools

def throw_dice():
    return random.randrange(1, 6)

def throw_until_doubles():
    
    throw_arr = []
    counter = 0
    
    while True:
        r1 = throw_dice()
        r2 = throw_dice()
        
        counter += 1
        
        if r1 == r2:
            break
    
    return counter

def main(num = 100):
    
    l1 = [throw_until_doubles() for i in range(0, num)]
    
    counter = functools.reduce(lambda a, b: a+b, l1)
    print("Average throws to reach doubles: %.2f" % round((counter / len(l1)), 2))
    
    return counter

print(f"Total throws: {main()}")