# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 16:34:47 2021

@author: 97250
"""

# Exercise 1

def form_pattern(ch1 = ' ', num1 = 2, ch2 = '*', num2 = 5):
    
    temp1 = ''.join([ch1 for i in range(0, num1)])
    temp2 = ''.join([ch2 for i in range(0, num2)])
    
    return (temp1 + temp2)


str_len = 5

for i in range(1, str_len+1):
    print(form_pattern('*', i, ' ', str_len-i))
    
while i > 0:
    print(form_pattern(' ', str_len-i, '*', i))
    i -= 1

# Exercise 2

my_list = [2, 24, 12, 354, 233, -1]

for i in range(len(my_list) - 1):
    minimum = i
    for j in range( i + 1, len(my_list)):
        if(my_list[j] < my_list[minimum]):
            minimum = j
            if(minimum != i):
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i] # non trivial sintaxis ... 
print(my_list)