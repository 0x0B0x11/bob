#!/bin/python3
#import tkinter                      # загрузка библиотеки tkinter
#tkinter._test()                     # отображение окна с тестом
from tkinter import *               # импортирование всех функций из библиотеки tkinter
root = Tk()
def Hello(event):
    print("Yet another hello world")

btn = Button(root,                  #родительское окно
             text="Click me",       #надпись на кнопке
             width=30,height=5,     #ширина и высота
             bg="white",fg="black") #цвет фона и надписи
btn.bind("<Button-1>", Hello)       #при нажатии ЛКМ на кнопку вызывается функция Hello
btn.pack()                          #расположить кнопку на главном окне
root.mainloop()