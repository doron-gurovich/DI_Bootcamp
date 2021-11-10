# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 14:03:09 2021

@author: 97250
"""

# Exercise 1 : Favorite Numbers

my_fav_numbers = {3, 5, 7, 9, 11}

my_fav_numbers.add(17)
my_fav_numbers.add(19)

my_fav_numbers_list = list(my_fav_numbers)
my_fav_numbers_list_lenght = len(my_fav_numbers_list)
my_fav_numbers.remove(my_fav_numbers_list[my_fav_numbers_list_lenght - 1])

friend_fav_numbers = {4, 6, 8, 10, 12}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

# Exercise 2: Tuple

# Given a tuple which value is integers, is it possible to add more integers to the tuple?
# well. we could add another tuple
# define a = (1, 2, 3) and b = (4, 5, 6) then 
# a + b = (1, 2, 3, 4, 5, 6) but this is not THE tuple. We here created a new one: c = a + b

# Exercise 3: Print A Range Of Numbers

list_of_floats_numbers = []

for i in range(0, 8):
    list_of_floats_numbers.append(0.5*(i+3))

# Exercise 5: Shopping List

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove(basket[0])
basket.remove(basket[-1])
basket.append("Kiwi")
basket.insert(0, "Apples")
basket.count("Apples")

basket.clear()

print(f"here is what we have in the basket: {basket}")

# Exercise 6 : Loop

my_name = "Doron"
test_name = ""

while test_name != my_name:
    test_name = input("please introduce yourself: ")
    
# Exercise 7

basket = ["Banana", "Apples", "Oranges", "Blueberries", "sdasd", "the last one"]
j = 0

for el in basket: # which is still not elegant. lets write it in an oldfashion way ...
    if j%2:
        j += 1
        continue
    print(f"{el}")
    j += 1


for i in range(0, len(basket)):
    if i%2:
        continue
    else:
        print(f"element# {i} : {basket[i]}")

# Exercise 8

for i in range(1500, 2500):
    if (i%5 == 0):
        print(f"integer {i} is multiple of 5")
    elif (i%7 == 0):
        print(f"integer {i} is multiple of 7")
    else:
        continue

# Exercise 9: Favorite Fruits

str_input_fruits = input("please input your favorite fruits separated with a single space: ")

l_input_fruits = str_input_fruits.split(" ")

str_some_specific_fruit = input("now please specify the fruit: ")

if str_some_specific_fruit in l_input_fruits:
    print(f"You chose {str_some_specific_fruit} one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")

# Exercise 10: Who Ordered A Pizza ?

str_topping = "pizza itself"
l_pizza_toppings = []
l_break_the_loop = ["quit", "stop", "enought"]

topping_cost = 2.5
pizza_cost = 10

while True:
    str_topping = input("please enter a series of pizza toppings now: ")
    
    if (str_topping in l_break_the_loop):
        break
    else:
        print(f"we will add ({str_topping}) to your pizza!")
        l_pizza_toppings.append(str_topping)

str_the_order = f"""

********************
we finally have pizza with following toppings:
{l_pizza_toppings}

====================

totally: US${pizza_cost + topping_cost*(len(l_pizza_toppings) - 1)}

********************

"""

print(str_the_order)    
    
    
# Exercise 11: Cinemax

price_for_age_0to3 = 0
price_for_age_3to12 = 10
price_for_age_12 = 15

i_price_per_age_for_family_members = 0

str_age_of_family_members = input("Ask a family the age of each person who wants a ticket: ")

split_age_of_family_members = str_age_of_family_members.split()

l_age_of_family_members = list(map(int, split_age_of_family_members))

for el in l_age_of_family_members:
    if el in range(0, 2):
        i_price_per_age_for_family_members += (price_for_age_0to3)
    elif el in range(3, 12):
        i_price_per_age_for_family_members += (price_for_age_3to12)
    else:
        i_price_per_age_for_family_members += (price_for_age_12)

print(f"the total price for your tickets is equal to {i_price_per_age_for_family_members}")


l_break_the_loop = ["quit", "stop", "enought"]

while True:
    str_movie = input("which movie do you want to watch? ")
    i_age = int(input("please enter your age: "))
    
    if (str_movie in l_break_the_loop):
        break
    else:
        if i_age in range(0, 16):
            print("you allowed to watch list#1")
        elif i_age in range(16, 21):
            print("you allowed to watch list#2")
        else:
            print("congrats! no restriction for you!")



# Exercise 12 : Who Is Under 16?

l_names = ["qwqw", "asas", "zxzx"]

l_break_the_loop = ["quit", "stop", "enought"]

while True:
    str_name = input("please insert your name: ")
    
    if (str_name in l_break_the_loop):
        break
    elif str_name in l_names:
        i_age = int(input("please insert your age:"))
        if i_age < 16:
            print("we have to remove your name from the list ...")
            l_names.remove(str_name)
    else:
        print("your name is not in the list. try again")


# Exercise 13 and Exercise 14

l_sandwich_orders = ["qwqw", "asas", "zxzx", "pastrami", "tuna"]
l_finished_sandwiches = []

l_break_the_loop = ["quit", "stop", "enought"]

while True:
    str_which_sandwich = input("please tell us which sandwich has been made: ")
    
    if (str_which_sandwich in l_break_the_loop):
        break
    elif str_which_sandwich in l_sandwich_orders:
        l_finished_sandwiches.append(str_which_sandwich)
    else:
        print("your sandwich was not found in the list. try again")

for el in l_finished_sandwiches:
    print(f"here is the the sandwich we made for you: {el}")

pastrami_count = l_finished_sandwiches.count("pastrami")
if pastrami_count >= 3:
    print(f"very nice! sandwich pastrami was found ({pastrami_count}) times in the list!")


print("now lets remove pastrami sandwiches ... ")

while l_finished_sandwiches.count("pastrami"):
    l_finished_sandwiches.remove("pastrami")

i_count_pastrami = l_finished_sandwiches.count("pastrami")
print(f"we have exactly {i_count_pastrami} pastrami sandwiches in the list")