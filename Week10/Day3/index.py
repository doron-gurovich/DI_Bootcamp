# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 10:00:58 2021

@author: 97250
"""

import json

json_file = './file.json'

with open(json_file, 'r') as file_obj:
    family = json.load(file_obj)

print(family)