# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 22:57:43 2021

@author: 97250
"""

from datetime import datetime
from time import strptime

i_candles = 0
str_candles = " "

str_birthdate = input("please specify your birthdate (mm/dd/yyyy): ")

date_today = datetime.today().strftime('%b %d %Y')
# date_birthdate = datetime.strptime(str_birthdate, '%b %d %Y').date()

l_date_today = date_today.split(' ')
l_date_birthdate = str_birthdate.split(' ')

i_candles = int(str(int(l_date_today[-1]) - int(l_date_birthdate[-1]))[-1])

if strptime(l_date_birthdate[0],'%b').tm_mon > strptime(l_date_today[0],'%b').tm_mon:
    i_candles -= 0
elif strptime(l_date_birthdate[1],'%d').tm_mday <= strptime(l_date_today[1],'%d').tm_mday:
    i_candles -= 0
else:
    i_candles -= 1

i_delta = int((12 - i_candles)/2)

for i in range(0, 11):
    
    if i < i_delta or (i_delta + i_candles) <= i:
        symbol = '_'
    else:
        symbol = 'i'
    
    str_candles += symbol

str_display = f"""

      {str_candles}
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~

"""

str_display += str_display if (int(l_date_birthdate[-1])%4 == 0 and int(l_date_birthdate[-1])%100 != 0) else ""

print(str_display)