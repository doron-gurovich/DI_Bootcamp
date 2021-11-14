# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 17:29:17 2021

@author: 97250
"""

num = int(input("please insert the test number: "))


l1 = [i for i in range(1, num) if num % i == 0]

if sum(l1) == num:
    print(f"congrats! {num} is a perfect number")
else:
    print("next time")


