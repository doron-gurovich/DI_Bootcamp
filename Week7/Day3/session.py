# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 18:11:45 2021

@author: 97250
"""

l1 = [i for i in range(0, 10)]

def func1(some_list):
    """
    Info: printing of the list
    """
    
    for el in some_list:
        print(el)
        
func1(l1)


import numbers
import decimal

my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]

def func_sum_arr(some_list):
    
    result = 0
    
    for num in some_list:
        try :
            result += num
        except TypeError:
            print('NaN, skipping')
    
    # temp_list = [num for num in some_list if  isinstance(num. numbers.Number)] 
    return result # sum(temp_list)

print(func_sum_arr(my_list))

people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]

l1 = list(map(len, people))

print("-----------------------------------")

for i in range(0, len(l1)):
    if l1[i] <= 4:
        print(f"hello {people[i]}")


zip_iterator = zip(people, l1)

for k, v in zip_iterator:
    if v <= 4:
        print(f"zip: {k}")