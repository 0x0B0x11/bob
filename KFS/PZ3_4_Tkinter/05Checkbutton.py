#!/bin/python3
from tkinter import *
from tkinter.messagebox import showinfo
def window_deleted():    
    print('Окно закрыто')    
    print("var1 =", var1.get(), "var2 =", var2.get())
    root.quit()        # явное указание на выход из программы
def checkbutton_changed():
    if var1.get() == 1:
        showinfo(title="Info", message="Включено")
    else:
        showinfo(title="Info", message="Отключено")
    
root=Tk() 
root.geometry('500x400+300+100') 
root.protocol('WM_DELETE_WINDOW', window_deleted) # обработчик закрытия окна

var1=IntVar() 
var2=IntVar() 

check1=Checkbutton(root,text=u'1 пункт',variable=var1,onvalue=1,offvalue=0, command=checkbutton_changed) 
check2=Checkbutton(root,text=u'2 пункт',variable=var2,onvalue=1,offvalue=0) 
check1.pack() 
check2.pack() 
root.mainloop() 
