# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 20:52:42 2021

@author: 97250
"""

str_input = input("please insert the string to reverse: ")

l1 = str_input.split(' ')

res = ""

for i in range(0, len(l1)):
    res += (l1[(len(l1) - 1) - i]) + ' '

print(res)