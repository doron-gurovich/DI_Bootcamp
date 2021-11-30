# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 20:18:33 2021

@author: 97250
"""

# Exercise 1 : Built-In Functions

num1 = 5
num2 = -5

if abs(num1) == abs(num2):
    print("abs() function is working!")
    
f_num3 = 3.14
num4 = int(f_num3)

print(f"float: {f_num3} vs integer: {num4}")

num5 = int(input("Enter the inputs : ") or "10")

print(f"Another option is str --> integer conversion. \nFor the input number we have {num5}")

# Exercise 2: Currencies

class Currency:
    
    """
    Info: Create the code which will output the results below.
    Hint: When adding 2 currencies which don’t share the same label you should raise an error.
    """
    
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
    
    def __str__(self):
        
        cur = self.currency + "s" if self.amount > 1 else self.currency
        
        return f"{self.amount} {cur}"
    
    def __int__(self):
        return self.amount

    def __repr__(self):
        cur = self.currency + "s" if self.amount > 1 else self.currency
        
        return f"{self.amount} {cur}"
    
    def __add__(self, cur, num = 0): # not yet clear how to add Currency element and integer number using the same method
        
        if self.currency == cur.currency:
            return self.amount + cur.amount
        else:
            raise TypeError("Cannot add between Currency type <dollar> and <shekel>")
            return -1

    def __iadd__(self, num): # __iadd__ is the correct dunder for += 
        return self.amount + num
        

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)