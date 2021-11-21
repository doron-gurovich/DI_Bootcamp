# -*- coding: utf-8 -*-

class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animal = {}
        
    def add_animal(self, animal_type, animal_count = 1):
        if animal_type in self.animal:
            self.animal[animal_type] += animal_count
        else:
            self.animal[animal_type] = animal_count
        
    def get_info(self):
        result = self.name + "'s farm\n\n"
              
        for k,v in self.animal.items():
            result += str(k) + ": "+ str(v) + "\n"
        
        
        return result

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_info())