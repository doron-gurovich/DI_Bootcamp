# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 21:35:52 2021

@author: 97250
"""

from tkinter import *
from tkinter import ttk


root = Tk()

frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

root.mainloop()


btn = ttk.Button(frm, ...)
print(btn.configure().keys())

def turn_red(self, event):
    event.widget["activeforeground"] = "red"

self.button.bind("<Enter>", self.turn_red)