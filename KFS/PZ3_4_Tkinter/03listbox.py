#!/bin/python3
from tkinter import *
def window_deleted():    
    print('Окно закрыто')    
    root.quit()                             # явное указание на выход из программы
def select_print():    
    selection = listbox2.curselection()     # мы можем получить выделенный элемент по индексу
    print("Выбран:", listbox2.get(selection[0], last = None), "(индекс", selection[0], ")")    
root=Tk() 
# --------------------------------- обработчик закрытия окна
root.protocol('WM_DELETE_WINDOW', window_deleted) 
# --------------------------------- Виджет Listbox: создание списков listbox1 и listbox2
listbox1=Listbox(root,height=8,width=16,selectmode=EXTENDED)
var_default = ["Севастополь", "Джанкой"]
list_var = StringVar(value=var_default)
listbox2=Listbox(root,height=8,width=16,selectmode=SINGLE, listvariable=list_var)
list1=[u"Москва",u"Санкт-Петербург",u"Саратов",u"Омск"]
list2=[u"Канберра",u"Сидней",u"Мельбурн",u"Аделаида"] 
for i in list1: 
	listbox1.insert(END,i) 
for i in list2: 
	listbox2.insert(END,i) 
listbox1.pack() 
listbox2.pack() 
# --------------------------------- Виджет Button: создание кнопки
button1=Button(root, text='Печать', width=8, height=1, bg='white', fg='black', font='arial 16', command=select_print) 
button1.pack() 

root.mainloop()
