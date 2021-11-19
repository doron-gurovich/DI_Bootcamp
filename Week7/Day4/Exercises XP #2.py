# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 20:27:19 2021

@author: 97250
"""

from datetime import datetime

def get_age(year, month, day):
    temp_date = datetime.today().strftime('%Y-%m-%d')
    date_today = temp_date.split('-')
    
    age_result = int(date_today[0]) - year
    
    if month < int(date_today[1]):
        age_result -= 1
    elif month == int(date_today[1]) and int(date_today[2]) < day:
        age_result -= 1
    
    return age_result

get_age(1980, 11, 7)

def can_retire(gender, date_of_birth):
    
    num_date_list = list(map(lambda s: int(s), date_of_birth.split('/')))
    
    my_age = get_age(*num_date_list)
    
    if gender == 'm' and my_age >= 67:
        return True
    elif gender == 'f' and my_age >= 62:
        return True
    else:
        return False

print(can_retire("m", "1950/11/07"))

#####################################################################################################

# importing functools for reduce()
import functools

def my_sum(num = 3, final_size = 4):
    """
    Info: Write a function that accepts one parameter (an int: X) and returns the value of X+XX+XXX+XXXX
    
    """
    
    temp_arr = [ i*str(num) for i in range(1, final_size+1)]
    
    result = functools.reduce(lambda s1, s2: int(s1) + int(s2), temp_arr)
    
    return result

print(my_sum())