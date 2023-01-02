#!/bin/python3
from tkinter import *
def select_print():    
    print("Выбран:", var.get(), "пункт")    
root=Tk() 
var=IntVar() 
rbutton1=Radiobutton(root,text='1 пункт',variable=var, value=1, command=select_print) 
rbutton2=Radiobutton(root,text='2 пункт',variable=var, value=2, command=select_print) 
rbutton3=Radiobutton(root,text='3 пункт',variable=var, value=3, command=select_print) 
rbutton1.pack() 
rbutton2.pack() 
rbutton3.pack() 
root.mainloop() 
