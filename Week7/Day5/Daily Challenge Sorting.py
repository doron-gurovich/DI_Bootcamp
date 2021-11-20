# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 18:21:43 2021

@author: 97250
"""

def string_sorting( *args ):
    
    result = list(args).copy()
    
    for j in range(0, max(list(map(len, result)))):
        
        try:
            iterator = [i for i in range(0, len(result))]
            
            input_list = list(zip(iterator, result))
            
            
            sort_first_letter = {el[0]: el[1][j] for el in input_list if len(el[1]) > j}
            sort_first_letter_res = {k: v for k, v in sorted(sort_first_letter.items(), key=lambda item: item[1])}
            
            temp_result = sort_first_letter_res.copy()        
            temp_result.update(dict(input_list))
            
            result = [*temp_result.values()]
            
        except:
            print("something went wrong")

    return result

print("sorted string: ", string_sorting("zxzx", "qwqw", "asas", "zxzx", "aassas", "aaasddsadgit"))
