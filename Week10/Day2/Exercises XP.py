# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 12:24:53 2021

@author: 97250
"""

# Exercises #1 and #2

from module_name import function_name as mn_fn

print(mn_fn(2))

# Exercises #3

import string
import random

N = 5

result = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(N))

print(f"Generate random String of length {N}: {result} ")