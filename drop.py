# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 07:27:05 2020

@author: bk406
"""

from tkinter import *

def function1():
    print("Menu item clicked")
    
root = Tk()

mymenu = Menu(root)
root.config(menu=mymenu)

submenu = Menu(mymenu)
mymenu.add_cascade(label="File", menu=submenu)

submenu.add_command(label="Project", command=function1)
submenu.add_command(label="Save", command=function1)

submenu.add_separator()
submenu.add_command(label="Exit", command=function1)

#Creating Another Menu Section  "EDIT"
newmenu = Menu(mymenu)
mymenu.add_cascade(label="Edit", menu=newmenu)
newmenu.add_command(label="Undo", command=function1)

root.mainloop()