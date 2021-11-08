# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Week 6, day 2
# Exercises XP

# exercise #1

str_HelloWorld = "Hello world"

for i in range(4):
    print(str_HelloWorld)
    
# exercise #2

x = (99^3) * 8

#exercise #3

"""
>>> 5 < 3    False
>>> 3 == 3   True
>>> 3 == "3" Error
>>> "3" > 3  Error
>>> "Hello" == "hello" False
"""

#exercise #4

str_computerBrand = 'HP'

print(f"I have an {str_computerBrand} computer")

#exercise #5 

str_name = "Doron"
i_age = 41
f_shoe_size = 46.5
str_info = f"my name is {str_name}, i'm {i_age} years old w/ shoe size {f_shoe_size}\nand i'm loving yoga"

print(str_info)

#exercise #6

a = 40
b = 20

if a > b:
    print("Hello World.")
    
# exercise #7

i_number = int(input("please insert some integer number here: "))

if i_number%2 == 0 and type(i_number) == int:
    print(f"your number {i_number} is even")
elif i_number%2 != 0 and type(i_number) == int:
    print(f"your number {i_number} is odd")
else :
    print(f"whatever you gave us {i_number} is not an int number")


#exercise #8
str_users_name = input("please insert your name here: ")

if str_users_name.lower() == str_name.lower():
    print(f"bingo! we have the same name: {str_name}")
else:
    print(f"this time names are different \nMy name is {str_name}\nYour name is {str_users_name}")

# exercise #9

i_users_height = int(input("please insert your height in inches here: "))

f_inch_to_cm_ratio = 2.54 

i_users_height_in_cm = i_users_height * f_inch_to_cm_ratio

if 145 < i_users_height_in_cm < 280:
    print(f"your are as tall as {i_users_height} inches or {i_users_height_in_cm} cm. \nTall enough to ride!")
elif 40 < i_users_height_in_cm <= 145 :
    print(f"your are as tall as {i_users_height} inches or {i_users_height_in_cm} cm. \nNot yet there ...")
else :
    print("please insert the relevant number")