# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 10:45:37 2021

@author: 97250
"""
# Exercise 1 : Concatenate Lists

l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]

l3 = l1 + l2

l4 = l1.copy()

for i in range(0, len(l2)):
    l4.append(l2[i])

if l3 == l4:
    print("we are done here")
else:
    print("hm ... something wrong")

# Exercise 2: Greatest Number

str_input = input("please insert 3x numbers separated by space: ")

l_input = str_input.split(' ')

l_input.sort()

print(f"the greatest number is: {l_input[-1]}")

# Exercise 3 : The Alphabet
import string

str_alphabet = string.ascii_lowercase

tuple_vowel_letters = ('a', 'e')