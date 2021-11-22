# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 20:35:13 2021

@author: 97250
"""

# Exercise 1: Cats

print("************************************************************************")

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat("QW", 1)
cat2 = Cat("AS", 2)
cat3 = Cat("ZX", 3)

cats_array = [cat1, cat2, cat3]

def the_oldest_cat(*args):
    
    temp = list(args).copy()
    temp_age = [c.age for c in temp]
    
    cats_with_age = list(zip(temp, temp_age))
    
    return [el[0] for el in cats_with_age if el[1] == max(temp_age)][0]
    

result = the_oldest_cat(*cats_array)

print(f"the oldest cat is: {result.name} and she/he is {result.age} years old.")

# Exercise 2 : Dogs

print("************************************************************************")

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")
    
    def jump(self):
        print(f"{self.name} jumps {2*(self.height)} cm high")


davids_dog = Dog("Rex", 50)

print(f"David's dog name is: {davids_dog.name}, and its {davids_dog.height} cm high")

davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)

print(f"Sarah's dog name is: {sarahs_dog.name}, and its {sarahs_dog.height} cm high")

sarahs_dog.bark()
sarahs_dog.jump()

heightest_dog = davids_dog if davids_dog.height > sarahs_dog.height else sarahs_dog

print(f"the heightest dog name is: {heightest_dog.name}")


# Exercise 3 : Who’s The Song Producer?

print("************************************************************************")

class Song:
    def __init__(self, *lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        # map(print, self.lyrics) -- doesnt really work ... 
        
        for el in self.lyrics:
            print(el)
        
        return True

txt = ["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven" ]

stairway = Song(*txt)
stairway.sing_me_a_song()

# Exercise 4 : Afternoon At The Zoo

print("************************************************************************")

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
    
    def add_animal(self, new_animal):
        if new_animal in self.animals:
            return False
        else:
            self.animals.append(new_animal)
            return True

    def get_animals(self):
        if not self.animals:
            print("the list is empty")
            return False
        else:
            for el in self.animals:
                print(el)
            return True
            
    
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            return True
        else:
            print(f"we don't have such animal ({animal_sold}) at the moment.")
            return False
    
    def sort_animals(self):
        
        if not self.animals:
            print("the list is empty")
            return False
        
        self.animals.sort()
        
        temp = [s[0] for s in self.animals]
        convolution_set = set(temp)
        convolution_set_counter = []
        
        i = 0
        
        for ch in convolution_set:
            # convolution_set_counter[i] = temp.count(ch)
            i += 1
        
        convolution_dict = dict(zip(list(convolution_set), list(convolution_set_counter)))
        
        sort_dict = {}
        sort_dict_len = 0
        sort_dict_counter = 0
        
        
        
        return sort_dict
    
    def get_groups(self):
        
        d1 = self.sort_animals()
        
        for k, v in d1.items():
            print(k, v)
        
        return True

ramat_gan_safari = Zoo("Ramat Gan Safari")

ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Anglerfish")
ramat_gan_safari.add_animal("Bernedoodle")
ramat_gan_safari.add_animal("Booby")
ramat_gan_safari.add_animal("Jackabee")
ramat_gan_safari.add_animal("Jerboa")
ramat_gan_safari.add_animal("Kangal")
ramat_gan_safari.add_animal("Siberpoo")
ramat_gan_safari.add_animal("Armadillo")
ramat_gan_safari.add_animal("Siamese")
ramat_gan_safari.add_animal("Zuchon")
ramat_gan_safari.add_animal("Dunker")
ramat_gan_safari.add_animal("Dragonfly")
ramat_gan_safari.add_animal("Lizard")
ramat_gan_safari.add_animal("Lemur")

ramat_gan_safari.get_animals()

print("++++++++++++++++++ let's sort animals now ++++++++++++++++++++++++++++++++")
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_animals()

print("++++++++++++++++++ let's get groups now ++++++++++++++++++++++++++++++++")
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()

print("************************************************************************")