#!/bin/python3
from tkinter import *
root=Tk()
def leftClick(event):
    print (u'Нажата левая кнопка мыши')
def midleClick(event):
    print (u'Нажата средняя кнопка мыши')
def rightClick(event):
    print (u'Нажата правая кнопка мыши')
def altMotion(event):
    print (u'Нажата клавиша <Alt> + перемещение мыши')
def mouse2Click(event):
    print (u'Двойной клик левой кнопкой мыши')
def mouse3Click(event):
    print (u'Тройной клик правой кнопкой мыши')
button1=Button(root, text=u'Нажми')
button1.pack()
button1.bind('<Button-1>', leftClick)
button1.bind('<Button-2>', midleClick)
button1.bind('<Button-3>', rightClick)
button1.bind('<Alt-Motion>', altMotion)
button1.bind('<Double-Button-1>', mouse2Click)
button1.bind('<Triple-Button-3>', mouse3Click)
root.mainloop()
