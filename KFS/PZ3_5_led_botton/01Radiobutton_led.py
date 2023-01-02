#!/bin/python3
# вначале подключим необходимую библиотеку
import RPi.GPIO as GPIO
# также понадобится библиотека, которая отвечает за ожидание (она нужна, чтобы установить интервал включения и выключения лампочки)
import time
from tkinter import *
# чтобы запустить GPIO, понадобится выполнить функцию GPIO.setmode
#GPIO.setmode(GPIO.BOARD)        #- тоже можно!
GPIO.setmode(GPIO.BCM)

# pins=[10, 33, 35]             # Ошибочно заданный пин для демонстрации примера
pins=19                         # подключение пина
# pins[0]=31                    # Исправляем ошибку
# print(pins)                   # Выводим список и видим, что все изменения отразились в списке

# теперь Python знает о GPIO, и ему можно указать на то, с каким портом нужно будет работать и что он должен делать (в данном случае – 11-м и он будет работать на выход)
GPIO.setup(pins, GPIO.OUT)      # Все пины в режим OUTPUT
def select_print():    
    if var.get() == 1:
        print("Включено")  
        values=1
        GPIO.output(pins,values)    # HIGH pin)  
    elif var.get() == 2:
        print("Выключено")  
        values=0
        GPIO.output(pins,values)    # LOW pin)  
    else:
        print("Завершено")  
        GPIO.output(pins,0)         # LOW pin)
        GPIO.cleanup() 			    # возвращаем пины в исходное состояние
        root.quit()                 # явное указание на выход из программы    
root=Tk() 
var=IntVar() 
rbutton1=Radiobutton(root,text='Включить                 ',variable=var, value=1, command=select_print) 
rbutton2=Radiobutton(root,text='Выключить              ',variable=var, value=2, command=select_print) 
rbutton3=Radiobutton(root,text='Закончить и выйти',variable=var, value=3, command=select_print) 
rbutton1.pack() 
rbutton2.pack() 
rbutton3.pack() 
root.mainloop() 
