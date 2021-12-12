# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 13:56:12 2021

@author: 97250
"""

from datetime import date
from datetime import datetime

# import holidays -- see comments to Exe #4 below

today = date.today()
print(f"today is: {today}")

def time_left_till(some_date = '31.12.21 23:59:59'):
    """
    Info: function that displays the amount of time left from now until <some_date>
    """
    
    today = datetime.now()
    some_day_obj = datetime.strptime(some_date, '%d.%m.%y %H:%M:%S')
    
    delta = some_day_obj - today
    
    return delta

def days_hours_minutes(td):
    return td.days, td.seconds//3600, (td.seconds//60)%60

delta = days_hours_minutes(time_left_till())

print(f"day left till NY: {delta[0]} days and {delta[1]} hours, {delta[2]} min.")


def how_long_did_u_live(bd = '07.11.80 20:59:59'):
    
    """
    Info: return result in min
    """
    
    bd_obj = datetime.strptime(bd, '%d.%m.%y %H:%M:%S')
    today = datetime.now()
    
    delta = today - bd_obj
    
    result = delta.days*24*60 + delta.seconds//60 + (delta.seconds//60)%60 # days in min + h --> min + min
    
    return result

print(f"you totally have ({how_long_did_u_live()}) min by now")


# Exercise 4: holidays module doesnt work. installation done
# import holidays gave an error: ModuleNotFoundError: No module named 'holidays'

def how_old_are_u(num, planet = "Earth"):
    
    year_to_sec = 31557600
    
    solar_sys_coeff = {
        "Earth": 1.0,
        "Mercury": 0.2408467,
        "Venus": 0.61519726,
        "Mars": 1.8808158,
        "Jupiter": 11.862615,
        "Saturn": 29.447498,
        "Uranus": 84.016846,
        "Neptune": 164.79132
    }
    
    k = year_to_sec * solar_sys_coeff[planet]
    
    return num / k

list_of_planets_in_solar_sys = ["Earth", "Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

for el in list_of_planets_in_solar_sys:
    print(f"on planet {el} you will be: {how_old_are_u(60*how_long_did_u_live(), el)} y.o.")
    
# same story as we have w/ holidays: installation doesnt work properly ...