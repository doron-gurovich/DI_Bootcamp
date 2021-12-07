# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 18:18:20 2021

@author: 97250
"""

f = open('./import/secret.txt')
# data = f.read()
# each_5_line = [l for l in data if (data.index(l)%5 == 0)]

Lines = f.readlines()
each_5_line = [l for l in Lines if not Lines.index(l)%5]

each_5_character = [l[4] for l in Lines if not Lines.index(l)%5]

d_count = Lines.count("Darth\n")
l_count = Lines.count("Luke\n")
Lea_count = Lines.count("Lea\n")

f.close()