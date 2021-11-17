# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 11:20:56 2021

@author: 97250
"""

# exercise #1

def display_message():
    print("i'm learning Full stack dev")
    
display_message()

# exercise #2

def favorite_book(title):
    print(f"One of my favorite books is {title}")

favorite_book("Alice in Wonderland")

# exercise #3

def describe_city(city, country):
    print(f"{city} is in {country}")

describe_city("Iceland", "Reykjavik ")

# exercise #4

import random

def my_random(i):
    j = random.randint(0, 100)
    str_res = f"these are the same numbers" if i == j else f"fail your guess was {i} \nwe have {j}"
    
    print(str_res)

my_random(10)

# exercise #5

def  make_shirt(size = 'L', text = 'Im loving Python'):
    str_welcome = "this is a default settings" if size == 'L' or size == 'M' else "different message"
    
    print(str_welcome)
    print(f"you about to order the shirt w/ size {size} and text: {text}")
    
make_shirt()
make_shirt(size = "(something)", text = "(something else)")

# exercise #6

list_of_magicians = ["David Copperfield", "Roy Rochlin", "Getty Images", "Rick Jay"]

def show_magicians(magicians):
    for magician in magicians:
        print(f"{magician}")

show_magicians(list_of_magicians)

def make_great(magicians):
    result = ["the great " + magician for magician in magicians]
    
    return result

show_magicians(make_great(list_of_magicians))