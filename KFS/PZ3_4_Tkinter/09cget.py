#!/bin/python3
from tkinter import *
from random import random
def button_clicked():
    #button['text'] = button['bg']      # показываем предыдущий цвет кнопки
    button['text'] = button.cget('bg')  # показываем предыдущий цвет кнопки
    bg = '#%0x%0x%0x' % (int(random()*16), int(random()*16), int(random()*16))
    button['bg'] = bg
    button['activebackground'] = bg
root=Tk()
button = Button(root, command=button_clicked)
button.pack()
root.mainloop()