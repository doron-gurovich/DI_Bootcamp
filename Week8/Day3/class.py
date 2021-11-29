# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 18:05:28 2021

@author: 97250
"""

class Circle:
    color = "red"

class NewCircle(Circle):
    color = "blue"

nc = NewCircle
print(nc.color)