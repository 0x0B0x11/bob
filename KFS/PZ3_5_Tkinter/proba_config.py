#!/bin/python3
# ================================================ Загружка библиотек
from tkinter import *

def clicked():
    lbl_welcome.configure(text="Welcome!!!")

root = Tk()
root.title("Welcome to the second entry app")
lbl_login = Label(root, text="Login")
lbl_pass = Label(root, text="Password")
lbl_welcome = Label(root)
txt1 = Entry(root, width=10)
txt2 = Entry(root, width=10)
btn = Button(root, text="Enter", command=clicked)
lbl_login.pack()
txt1.pack()
lbl_pass.pack()
txt2.pack()
btn.pack()
lbl_welcome.pack()
root.mainloop()