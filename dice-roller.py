'''
Austin Richards 1/23/21 14:51
'''

import random as rand
from tkinter import *

gui = Tk()
gui.title("Dice Roller 2000")

# make the display
display = Entry(gui, width=40, borderwidth=2)
display.grid(row=0, column=0)

# functions for buttons
def d100():
    display.delete(0, END)
    roll_val = rand.random() * 100
    roll_val = round(roll_val)
    display.insert(0, str(roll_val))

def d10():
    display.delete(0, END)
    roll_val = rand.random() * 10
    roll_val = round(roll_val)
    display.insert(0, str(roll_val))

def d6():
    display.delete(0, END)
    roll_val = rand.uniform(1,6)
    roll_val = round(roll_val)
    display.insert(0, str(roll_val))

def d4():
    display.delete(0, END)
    roll_val = rand.uniform(1,4)
    roll_val = round(roll_val)
    display.insert(0, str(roll_val))

# make the buttons
but_100 = Button(gui, text="d100", command=d100)
but_10  = Button(gui, text="d10", command=d10)
but_6   = Button(gui, text="d6", command=d6)
but_4   = Button(gui, text="d4", command=d4)

# put the buttons in the window
but_100.grid(row=1, column=0, sticky="nsew")
but_10.grid(row=2, column=0, sticky="nsew")
but_6.grid(row=3, column=0, sticky="nsew")
but_4.grid(row=4, column=0, sticky="nsew")

gui.mainloop()