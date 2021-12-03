# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 20:31:36 2021

@author: 97250
"""

ask_input = 5
l1 = []

for i in range(ask_input):
    name = input("please introduce yourself: ")
    age = int(input("how old are you: "))
    score = int(input("score: "))
    
    temp_tuple = (name, age, score)
    
    l1.append(temp_tuple)

print(f"input: {l1}")

l1.sort(key = lambda el: (el[0], el[1], el[2]))

print(f"sorted result #2: {l1}")