# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 17:04:23 2021

@author: 97250
"""

import translator

french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]

for el in french_words:
    
    print(f"{el}, {translator.translator_dict[el]}")
