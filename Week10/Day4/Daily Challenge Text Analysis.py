# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 17:23:53 2021

@author: 97250
"""

class Text():
    
    def __init__(self, string):
        self.string = string
    
    def frequency_of_word(self, some_word):
        pass
    
    def the_most_common_word(self):
        pass
    
    def list_of_unique_words(self):
        pass
    
    def test_instance(self):
        """
        Not sure i understand the task here
        """
    
    def info(self):
        pass

class TextModification(Text):
    
    def __init__(self, string):
        super().__init__(string)
        
    def remove_symbols(self, *args):
        pass
    
    def no_punctuation(self):
        pass
    
    def no_stop_words(self):
        pass
    
    def no_special_characters(self):
        pass

filename = "./the_stranger.txt"

with open(filename) as file:
    result = file.readlines()
    result = [line.rstrip() for line in result]
 
file.close()