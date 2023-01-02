#!/bin/python3
from tkinter import *               # импортирование всех функций из библиотеки tkinter
root1 = Tk()
root2 = Tk()
root1.after(500, root1.mainloop) # первый цикл запускаем в фоне
root2.mainloop()