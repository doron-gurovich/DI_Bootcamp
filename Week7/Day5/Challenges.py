# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 17:28:00 2021

@author: 97250
"""

# Exercise 1

def insert_item_in_a_list(item, index, *args):
    
    """
    Info: Write a script that inserts an item at a defined index in a list.
    """
    result = list(args).copy()
    
    result[index] = item
    
    return result

list_t1 = [1, 2, 3, 'q', 'a', 'z']

print(insert_item_in_a_list('item', 2, *list_t1))

# Exercise 2

def count_symbol_in_a_string(string, ch = ' '):
    
    """
    Info: Write a script that counts the number of spaces in a string
    """
    
    result = 0
    
    for i in range(len(string)):
        if string[i] == ch:
            result += 1
            
    return result

sentence = """


Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi cursus massa quam, eget interdum lacus congue sed. Suspendisse risus lectus, fermentum hendrerit commodo a, vehicula porta nibh. Pellentesque interdum augue orci, sed porta dolor ultricies eu. Vestibulum viverra odio metus, nec pretium dolor efficitur at. Fusce pretium lorem ante. Praesent ac ultricies erat. Etiam cursus, justo eu accumsan luctus, justo lorem congue tortor, ut tincidunt purus tellus at nisl.

Ut dignissim nec risus in efficitur. Etiam vestibulum sapien consequat elementum porttitor. In rhoncus ultrices ante, vel commodo erat lobortis nec. Vivamus in ligula sed dolor dictum volutpat eu et orci. Fusce placerat tellus molestie libero congue, vitae euismod augue ultricies. Pellentesque pharetra lorem quis magna porta, sit amet placerat neque suscipit. Duis sit amet molestie nunc, a convallis mi.

Mauris et erat ut enim ornare imperdiet eget non purus. Phasellus eu tortor et arcu posuere commodo ac eu nulla. Nam vestibulum nisl sem, et cursus erat aliquam ac. Mauris eget sapien tincidunt metus rhoncus efficitur tempor vitae orci. Sed ultrices enim sit amet lectus volutpat blandit sed vitae est. Morbi elementum lacus et mollis pellentesque. Nunc fringilla lobortis tristique. Nunc ex lacus, ultricies vel libero non, lobortis congue felis. Suspendisse pretium laoreet neque ut finibus. Sed vitae justo consectetur, accumsan tellus at, iaculis augue. Etiam volutpat ultricies urna, porta tincidunt sem. Suspendisse eget lectus et nunc rutrum euismod id ac sem. Proin eget viverra ex. Duis ullamcorper dapibus elit, vitae laoreet velit egestas vel.

Fusce vulputate lorem vitae leo faucibus, ac eleifend justo euismod. Curabitur laoreet luctus viverra. Donec egestas rhoncus fermentum. Nam sed ornare nunc. Proin dapibus nisl augue, eget porta augue efficitur euismod. Nunc vel dictum lacus. Vestibulum lectus nulla, posuere eget ex et, volutpat blandit ante. Nulla gravida congue metus ac auctor. Phasellus ultricies dolor et purus blandit, ac malesuada dolor placerat. Curabitur vitae finibus nisl. Curabitur cursus nisi posuere est vestibulum imperdiet. Suspendisse potenti. Morbi sollicitudin nibh et metus maximus consequat. Fusce ultricies libero sit amet ante tincidunt mattis. Vestibulum eu dui nibh.

Integer elementum tempor elit vitae cursus. Pellentesque hendrerit id massa et vulputate. Cras et cursus sem. Donec non suscipit mauris. Aliquam erat volutpat. Mauris vitae dui sit amet velit venenatis malesuada. Suspendisse facilisis eu mauris id tristique. Sed volutpat arcu ullamcorper cursus sollicitudin. Quisque vel tellus ut dolor semper faucibus a eu felis. Cras tempor bibendum dolor non faucibus. Integer volutpat, mi a posuere dapibus, metus sem ornare justo, sit amet vehicula metus justo at metus. Vivamus pretium, risus sed lobortis porta, eros arcu lobortis nisi, id viverra nunc lacus ut sapien.


"""

if sentence.count(' ') == count_symbol_in_a_string(sentence):
    print(f"we are done. there are {count_symbol_in_a_string(sentence)} of spaces in this sentence.")
    

# Exercise 3

def count_upper_symbol_in_a_string(string):
    
    """
    Info: Write a script that calculates the number of upper case letters in a string.
    """
    
    result = 0
    
    for i in range(len(string)):
        if string[i].isupper():
            result += 1
            
    return result

print(f"there are {count_upper_symbol_in_a_string(sentence)} upper case letters in this sentence.")


def count_lower_symbol_in_a_string(string):
    
    """
    Info: Write a script that calculates the number of lower case letters in a string.
    """
    
    result = 0
    
    for i in range(len(string)):
        if string[i].islower():
            result += 1
            
    return result

print(f"there are {count_lower_symbol_in_a_string(sentence)} upper case letters in this sentence.")


# Exercise 14

def dict_avg(**kwargs):
    
    """
    Info: Write a function that returns the average value in a dictionary (assume the values are numeric)
    """
    
    result = 0
    
    l1 = list(kwargs.values())
    
    result = sum(l1) / len(l1)
    
    return result

d1 = {'a': 1,'b':2,'c':8,'d': 1}

print(f"the average value in a dictionary is: {dict_avg(**d1)}")


# Exercise 15

def common_div(num1 = 10, num2 = 20):
    
    """
    Info: 
    """
    
    result = []
    
    for i in range(2, min(num1, num2) + 1):
        if num1%i == 0 and num2%i == 0:
            result.append(i)
    
    return result

print(common_div())

# Exercise 16

def is_prime(num = 100):
    
    """
    Info: Write a function that test if a number is prime
    """
    
    result = True
    
    for i in range(2, num):
        if num%i == 0:
            result = False
    
    return result

print(f"check if 100 is a prime number: {is_prime()}")
print(f"check if 17 is a prime number: {is_prime(17)}")

def prime_arr(num = 100):
    
    """
    Info: return all prime numbers between 0 and num (including num)
    """
    
    result = []
    
    for i in range(2, num+1):
        if is_prime(i):
            result.append(i)
            temp = i
        else:
            result.append(temp)
    
    return result

import numpy as np
import matplotlib.pyplot as plt

N = 10

X_axis = [i for i in range(1, N)]

plt.plot(X_axis, prime_arr(N), c='r', label='data')
plt.plot(X_axis, X_axis, c='b', label='data')

# naming the x axis
plt.xlabel('integers')
# naming the y axis
plt.ylabel('prime numbers')
 
# giving a title to my graph
plt.title('prime numbers distribution function')
 
# function to show the plot
plt.show()

plt.close('all')

##################### simple histogram 

# plt.bar(range(N), prime_arr(N))

# plt.bar(np.arange(0., 1.4, .2), [1, 2, 3, 4, 3, 2, 1], width=0.2)