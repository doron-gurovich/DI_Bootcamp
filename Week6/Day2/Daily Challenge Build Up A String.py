# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 13:26:06 2021

@author: 97250
"""

import random

str_text = input("please insert 10 characters long string: ")
# this string is tooooo long
# characters

i_length = len(str_text)

if i_length > 10:
    print("the string too long")
elif i_length < 10:
    print("the string is not long enough")
else:
    print(f"this is exactly what we need! \nthe first character is {str_text[0]}. \n the last character is {str_text[i_length - 1]}")


temp = ""

for i in range(i_length):
    temp += str_text[i]
    print(f"{temp}")
    
list_temp = list(temp)
random.shuffle(list_temp)
temp = ''.join(list_temp)


print(f"Finally we have a swaped string: {temp}. \nInitial string was: {str_text}")