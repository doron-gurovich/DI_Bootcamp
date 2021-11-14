# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 16:01:55 2021

@author: 97250
"""

import string

str_action = input("lets define the action: do you want encript or decript: ")
i_shift = int(input("lets define the shift: "))
str_input = input("please insert the test string (lowercase only so far): ")

i_shift *= 1 if str_action == "encript" else -1

alphabet = list(string.ascii_lowercase)

caesar_shift = {i: chr(ord(i) + i_shift) for i in alphabet if (ord(i) + i_shift) <= ord('z')}
caesar_shift1 = {i: chr(ord(i) + i_shift + ord('a') - ord('z') - 1) for i in alphabet if (ord(i) + i_shift) > ord('z')}
caesar_shift.update(caesar_shift1)


res = ""

for i in range(0, len(str_input)):
    res += caesar_shift[str_input[i]]

print(res)