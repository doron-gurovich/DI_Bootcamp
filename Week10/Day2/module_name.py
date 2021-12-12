# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 13:37:17 2021

@author: 97250
"""

import random

def function_name(num):
    r = random.randint(0, 10)
    
    result = f"excelent, we have exactly the same number: {r}" if r == num else f"({r} vs. {num}) try again"
    
    return result