# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 18:31:32 2021

@author: 97250
"""

class Door:

	objs = 0
	list_of_doors = [] # [ d0, d1, d2, d3 ]

	def __init__(self, locked):
		Door.list_of_doors.append(self)
		Door.objs += 1

		self.id = Door.objs
		self.locked = locked

	@property
	def next(self):
		return Door.list_of_doors[self.id:]

	def can_go_to(self, other_door):
		next_doors = self.next # [d2, d3]

		for i in range(len(next_doors)):

			if next_doors[i].locked == False:
				return False

			# did I reached to the destination door
			if next_doors[i] == other_door:
				return True

		return False


d1 = Door(True)

"""
objs = 1
list_of_doors = [ d1 ]

"""

d2 = Door(True)
"""
objs = 2
list_of_doors = [ d1, d2 ]
"""

d3 = Door(True)
"""
objs = 3
list_of_doors = [ d1, d2, d3 ]
"""

print(d1.next)
print("d1 --> d3", d1.can_go_to(d3))


# | | | |

print(d1 == d1)
print(d1 == d2)