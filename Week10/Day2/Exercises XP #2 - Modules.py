# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 13:56:12 2021

@author: 97250
"""

from datetime import date
from datetime import datetime

import holidays

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
    
    bd_obj = datetime.strptime(bd, '%d.%m.%y %H:%M:%S')
    today = datetime.now()
    
    delta = today - bd_obj
    
    result = delta.days*24*60 + delta.seconds//60 + (delta.seconds//60)%60 # days in min + h --> min + min
    
    return result

print(f"you totally have ({how_long_did_u_live()}) min by now")


