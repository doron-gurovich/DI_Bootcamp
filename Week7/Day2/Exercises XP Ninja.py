# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 13:18:34 2021

@author: 97250
"""

# exercis #2

l1 = ["qw", "qwqw", "qwqwqw", "as", "zx"]

def box_printer( *args ): 
    
    str_hat = ''.join(['*' for i in range(0, len(max(args, key=len)) + 3)])
    str_res = "".join(str_hat + "\n")

    
    for a in args[:]:
        temp = ''.join([' ' for i in range(0, 1 + len(max(args, key=len)) - len(a))])
        str_res += '*' + a + temp + '*\n'
    
    str_res += str_hat
    
    return str_res

print(box_printer("qw", "qwqw", "qwqwqw", "as", "zx", "asdasdasdfasdf"))

# exercis #2

# Ascending sorting is the purpose. chenged to descending sorting

def insertion_sort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1] < currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertion_sort(alist)
print(alist)