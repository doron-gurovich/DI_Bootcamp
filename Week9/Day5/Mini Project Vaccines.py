# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 10:41:00 2021

@author: 97250
"""

class Human():
    
    blood_type_list = ["A", "B", "AB", "O"]
    
    def __init__(self, id_number, name, age, blood_type):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.prioritary = False
        
        self.blood_type = [el for el in Human.blood_type_list if el == blood_type]
        
        # have to mention here: quite naive code is published.
        # any input variations will break the execution
        # no type checks or typo exception has been implemented here
        
        self.family = []
        
    def add_family_member(self, other):
        
        """
        Info: This method adds the person to this human’s family 
        and this human to the person’s family.
        """
        
        self.family.append(other)
        other.family.append(self)
        
        return True
    
    def info(self):
        
        family_str = str([(el.name, el.age) for el in self.family])
        
        print(f"""
              name and age of the persnon: {self.name}, {self.age}
              family: {family_str}
              """)
    def set_priority(self, priority):
            
        self.prioritary = priority
        
        return True
    
    def isSameFamily(self, other):
        
        result = False
        
        if self in other.family:
            result = True
            
        return result

class Queue():
    
    def __init__(self):
        self.humans = []
        
    def info(self):
        
        humans_list_of_names = str([(el.name, el.age) for el in self.humans])
        
        print(f"""
              who is in Queue: {humans_list_of_names}
              """)
              
        return True
    
    def add_person(self, other):
        
        """
        Info: Add a human to the queue, 
        if he is older than 60 years old or a prioritary person, 
        put him at the beginning of the list (at index 0) before every other.
        """
        
        if type(other) == Human:
            
            if other.age >= 60 or other.prioritary:
                self.humans.insert(0, other)
            else:
                self.humans.append(other)
            return True
        else:
            raise TypeError("TypeError: check the type of the argument")
            return False
        
    def find_in_queue(self, other):
        
        """
        Info: Returns the index of a human in the queue.
        """
        
        if type(other) == Human:
            if other in self.humans:
                return ''.join([el.id_number for el in self.humans if el == other])
            else:
                return f"(mentioned person {other.name} is not in Queue yet)"
        else:
            raise TypeError("TypeError: check the type of the argument")
            return False
    
    def swap(self, other1, other2):
        
        """
        Info: Swaps person1 with person2.
        """
        if other1 in self.humans and other2 in self.humans:
            
            temp1 = self.humans.index(other1)
            temp2 = self.humans.index(other2)
                    
            self.humans[temp1], self.humans[temp2] = self.humans[temp2], self.humans[temp1]
            
            # how cute is that ?! :)
            
            return True
        else:
            return f"(mentioned person {other1.name} or {other2.name} is not in Queue yet)"
    
    def get_next(self):
        
        """
        Info: return the next human in the queue, 
        meaning the object at index 0 in the list.
        
        Every human returned by get_next and get_next_blood_type 
        is removed from the list, 
        those functions return None if there is no one in the list.
        """
        
        if not self.humans:
            raise ValueError("ValueError: well the list is empty")
        else:
            el = self.humans[0]
            self.humans.remove(el)
            return el
    
    def get_next_blood_type(self, blood_type):
    
        """
        Info: Return the first human with this specific blood type.
        
        Every human returned by get_next and get_next_blood_type 
        is removed from the list, 
        those functions return None if there is no one in the list.
        """
        
        if blood_type in Human.blood_type_list:
            for el in self.humans:
                if ''.join(el.blood_type) == blood_type:
                    self.humans.remove(el)
                    return el
        else:
            raise ValueError("ValueError: there is no such blood type")
            return False
    
    def sort_by_age(self):
        
        """
        Info: Sort the queue so that the older ones are before the younger 
        ones and all the prioritary persons are before the others.
        """
        
        for i in range(len(self.humans)):
            for j in range(len(self.humans)):
                if self.humans[i].age > self.humans[j].age:
                    self.humans[i], self.humans[j] = self.humans[j], self.humans[i]
        
        return True
    
    def rearange_queue(self):
        
        """
        Info: Add the rearange_queue(self) method to the Queue class, 
        so that there is no two members of the same family one after the other.
        """
        
        result = []
        
        for i in range(len(self.humans)):
            for j in range(len(self.humans)):
                if self.humans[i].isSameFamily(self.humans[j]):
                    print("same family")
                    
                    # need to think how to realizde it ... taking family size into account
                    
        return result

h1 = Human("A12", "Asdf", 23, "A")
h2 = Human("B12", "Bsdf", 65, "AB")
h3 = Human("C12", "Csdf", 43, "B")
h4 = Human("A23", "Asdf", 70, "A")
h5 = Human("B23", "Bsdf", 80, "A")
h6 = Human("C23", "Csdf", 16, "O")
h7 = Human("D23", "Dsdf", 56, "B")
h8 = Human("E23", "Esdf", 8, "AB")
h9 = Human("A45", "Zxxx", 23, "O")

h2.set_priority(True)
h4.set_priority(True)
h6.set_priority(True)

h1.add_family_member(h2)
h1.add_family_member(h3)

h4.add_family_member(h5)
h4.add_family_member(h6)
h4.add_family_member(h7)
h4.add_family_member(h8)

h1.info()
h4.info()

q1 = Queue()

q1.add_person(h1)
q1.add_person(h2)
q1.add_person(h3)
q1.add_person(h4)
q1.add_person(h5)
q1.add_person(h6)
q1.add_person(h7)
q1.add_person(h8)

print(f"who is in queue by ID: {q1.find_in_queue(h2)}, {q1.find_in_queue(h6)}, {q1.find_in_queue(h9)}")

q1.info()

q1.swap(h1, h8)

print("--------------- swap ---------------")

q1.info()

q1.sort_by_age()

print("--------------- sort ---------------")

q1.info()

q1.get_next_blood_type("A")

# print(f"who was the next one with ({A}) blood type: {q1.get_next_blood_type(A).info()}")

print("--------------- get next blood type ---------------")

q1.info()

q1.get_next()

# print(f"who was the next one with ({A}) blood type: {q1.get_next_blood_type(A).info()}")

print("--------------- get next in line ---------------")

q1.info()

q1.rearange_queue()