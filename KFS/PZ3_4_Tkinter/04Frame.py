#!/bin/python3
from tkinter import *
root=Tk() 
frame1=Frame(root,bg='green',bd=3) 
frame2=Frame(root,bg='red',bd=3) 
button1=Button(frame1,text=u'Первая кнопка')
button2=Button(frame2,text=u'Вторая кнопка') 
frame1.pack() 
frame2.pack() 
button1.pack() 
button2.pack() 
root.mainloop()
