# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 13:07:53 2021

@author: 97250
"""

# Exercise 1 : Convert Lists Into Dictionaries

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dict1 = zip(keys, values)

print(tuple(dict1))

# Exercise 2 : Cinemax #2

price_for_age_0to3 = 0
price_for_age_3to12 = 10
price_for_age_12 = 15

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


def func_family_price(f):
    res = f.copy()
    
    for k, v in f.items():
        if 0 <= v < 3:
            res[k] = price_for_age_0to3
        elif 3 <= v < 12:
            res[k] = price_for_age_3to12
        else:
            res[k] = price_for_age_12
    
    return res

family_price = func_family_price(family)

family_price_sum = sum(list(family_price.values()))

print(family, '\n', family_price, '\n', f"totally: US${family_price_sum}")

# Exercise 3: Zara

brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': "Amancio Ortega Gaona" ,
    "type_of_clothes": ["men", "women", "children", "home" ],
    "international_competitors": ["Gap", "H&M", "Benetton" ],
    "number_stores": 7000,
    "major_color": {
        "France": "blue", 
        "Spain": 'red', 
        "US": ['pink', 'green']
        }
    }

brand_zaraza = brand.copy()

brand_zaraza["number_stores"] = 2

l1 = list(brand["type_of_clothes"])

print(f"Zara's clients are: {l1}")

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

the_last_competitor = brand["international_competitors"][-1]

print(f"the last competitor: {the_last_competitor}")

l2 = list(brand["major_color"]["US"])

print(f"the major clothes colors in the US are: {l2}")

print(f"brand len is: {len(list(brand.keys()))} \nand consist from: {list(brand.keys())}")


more_on_zara = {
    'creation_date': 1975,
    "number_stores": 10000
    }


# Exercise 4 : Disney Characters

users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]

disney_users_A = {users[n]: n for n in range(0, len(users))}
print(disney_users_A)

disney_users_B = {n: users[n] for n in range(0, len(users))}
print(disney_users_B)

users.sort()
disney_users_C = {n: users[n] for n in range(0, len(users))}
print(disney_users_C)


disney_users_D = {users[n]: n for n in range(0, len(users)) if (users[n].find('i') != -1) }
print(disney_users_D)

disney_users_E = {users[n]: n for n in range(0, len(users)) if users[n].lower().find('m') == 0 or users[n].lower().find('p') == 0}
print(disney_users_E)















