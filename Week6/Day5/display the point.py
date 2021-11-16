# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 21:14:15 2021

@author: 97250
"""

import matplotlib.pyplot as plt
x = [1, 1.5, 2]
y = [1, 2, 1]
plt.plot(x, y, 'ro')
plt.axis([0, 3, 0, 3])

for i_x, i_y in zip(x, y):
    plt.text(f"{i_x} {i_y}")

plt.show()