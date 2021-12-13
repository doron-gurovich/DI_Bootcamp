# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 21:02:35 2021

@author: 97250
"""

# Exersise #1

import random

def get_words_from_file(filename = "./random sentence generator.txt"):
    
    """
    Info: This function read the file’s content and return the words as a collection. 
    What is the correct data type to store the words?: <list>
    """
    
    with open(filename) as file:
        result = file.readlines()
        result = [line.rstrip() for line in result]
    
    file.close()
    
    return result
    
def get_random_sentence(length, *args):
    
    """
    Info: takes a single parameter called length. 
    The length parameter will be used to determine how many words the sentence should have. 
    The function should:
        -- use the words list to get your random words. 
        -- the amount of words should be the value of the length parameter.
    """
    
    input_list_of_words = list(args).copy()
    
    result = ' '.join([random.choice(input_list_of_words) for _ in range(length)])
    
    return result.capitalize() + '.'

def main():
    
    """
    Info: In this exercise we will create a random sentence generator. 
    We will do this by asking the user how long the sentence should be and then printing the generated sentence.
    returns boolean: True in case of proper execution
    """
    
    print(help(main))
    
    try:
        x = int(input("Ask the user how long they want the sentence to be (0, 20): "))
        
        if x in range(0, 20):
            print(get_random_sentence(x, *get_words_from_file()))
        else:
            print("the value is not in range: please insert integer number between 0 and 20")
            return False
    except ValueError:
        print("ValueError: please insert integer number between 0 and 20")
        return False
    
    return True

print(main()) # main returns boolean