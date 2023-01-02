#!/bin/python3
from tkinter import *
def window_deleted():    
    print('Окно закрыто')    
    name = entry1.get()
    print(name)
    root.quit()        # явное указание на выход из программы
root=Tk()
root.title('Пример приложения')
# --------- геометрические параметры: ширина=500, высота=400; расположение  x=300, y=200
root.geometry('500x400+300+100') 
# --------------------------------- обработчик закрытия окна
root.protocol('WM_DELETE_WINDOW', window_deleted) 
# --------------------------------- размер окна может быть изменён только по горизонтали
root.resizable(True, False) 
# --------------------------------- Виджет Button: создание кнопки
button1=Button(root, text='ok', width=15, height=3, bg='white', fg='red', font='arial 16') 
button1.pack() 
# --------------------------------- Виджет Label: создание надписи
label1=Label(root, width=30, text="Введите имя", fg='black', bg='green', font='courier 14')
label1.pack()
# --------------------------------- Виджет Entry: создание строки для ввода текста
entry1=Entry(root, width=30, fg="blue", bg="white", font='courier 14')
entry1.insert(0,'Иванов Сергей')
#root.Entry(root, width=30, text="Иванов Сергей", fg="blue", bg="white", font='courier 14')
entry1.pack()

root.mainloop()