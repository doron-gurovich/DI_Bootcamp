# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 20:41:11 2021

@author: 97250
"""

class X(): pass
class Y(): pass
class Z(): pass

class A(X, Y): pass
class B(Y, Z): pass

class M(A, B, Z): pass

print(M.mro())