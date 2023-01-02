#!/bin/python3
from tkinter import *
def window_deleted():    
    print('Окно закрыто')    
    root.quit()        # явное указание на выход из программы
root=Tk()
root.title('Пример приложения')
# геометрические параметры: ширина=500, высота=400; расположение  x=300, y=200
root.geometry('500x400+300+100') 
# ------------------------------------------------------------------------------ обработчик закрытия окна
root.protocol('WM_DELETE_WINDOW', window_deleted) 
# --------------------------------- размер окна может быть изменён только по горизонтали
root.resizable(True, False) 
root.mainloop()

