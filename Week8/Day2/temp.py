# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 19:48:41 2021

@author: 97250
"""

iterator = [i for i in range(0, len(self.animals))]
first_letters = [ch[0] for ch in self.animals]

a_list = list(zip(self.animals, iterator))
first_letters_list = list(zip(first_letters, iterator))

d1 = dict(first_letters_list)
l1 = list(d1.keys())
l1.sort()

for k1, v1 in d1.items():
    for l in l1:
        if k1 == l:
            print()
            
            
            
            
            for s in self.animals:
                for t in temp:
                    if s[0] == t[0]:
                        sort_dict[i] = t
                        temp.remove(t)
                        
                i += 1
                

for s in self.animals:
    for k, v in convolution_dict.items():
        sort_dict_counter += 1
        if s[0] == k:
            for j in range(sort_dict_len, sort_dict_len + v):
                sort_dict[sort_dict_counter].append()