#!/bin/python3
# ================================================ Загружка библиотек
import RPi.GPIO as GPIO
import time
from tkinter import *
# ================================================ Определение функций
def window_deleted():    
    print(' Завершено')    
    GPIO.output(pins,0)             # LOW pin)
    GPIO.cleanup() 			        # возвращаем пины в исходное состояние
    pwm.stop()
    root.quit()                     # явное указание на выход из программы
def func1():    
    if entry1.get() == " Включить":
        pwm.start(scale1.get())     # запускаем ШИМ на пине с коэффицентом заполнения 0-100%
    elif entry1.get() == " Выключить":
        pwm.stop()                  # останавливаем ШИМ
    else:
        print("Введено:", entry1.get(), "нужно: Включить / Выключить")
def func2():    
    if spinbox1.get() == " Включить":
        pwm.start(scale1.get())     # запускаем ШИМ на пине с коэффицентом заполнения 0-100%
    elif spinbox1.get() == " Выключить":
        pwm.stop()                  # останавливаем ШИМ
    else:
        print("Введено",spinbox1.get())
def func3():    
    selection = listbox1.curselection()     # получить выделенный элемент по индексу
    if selection == ():
        print('Не выбран элемент из списка')
    elif listbox1.get(selection[0]) == " Включить ":
        pwm.start(scale1.get())     # запускаем ШИМ на пине с коэффицентом заполнения 0-100%
    else:
        listbox1.get(selection[0]) == " Выключить "
        pwm.stop()                  # останавливаем ШИМ
def func4():    
    if varC.get() == 1:
        pwm.start(scale1.get())     # запускаем ШИМ на пине с коэффицентом заполнения 0-100%
    elif varC.get() == 0:
        pwm.stop()                  # останавливаем ШИМ
def func50():
    pwm.stop()                      # останавливаем ШИМ
def func51():
    pwm.start(scale1.get())         # запускаем ШИМ на пине с коэффицентом заполнения 0-100%
def func6(): 
    pwm.stop()                      # останавливаем ШИМ
    time.sleep(0.01)
    if varR.get() == 1:
        GPIO.output(pins, 1)        # HIGH pin
    elif varR.get() == 0:
        GPIO.output(pins, 0)        # LOW pin
def func7(val):
    a = scale1.get()
    pwm.ChangeDutyCycle(a)          # изменяем коэффициент заполнения
def func8(channel):
    global fl
#    print(label1.cget('bg'))
#    print(label1.cget('fg'))
    if fl == 0:
        label1.config(background = "yellow")
        label1.config(foreground = "#B71C1C")
        varE.set( ' Включить ')
        varSp.set( ' Включить ')
        listbox1.select_set(first=0, last=0)
        listbox1.select_clear(first=1, last=1)
        varC.set(1)
        varR.set(1)

        varL.set(' Включено ')
        GPIO.output(pins, 1)        # HIGH pin
        fl = 1
    else:
        label1.config(background = "#d9d9d9")
        label1.config(foreground = "#000000")
        varE.set(' Выключить ')
        varSp.set( ' Выключить ')
        listbox1.select_set(first=1, last=1)
        listbox1.select_clear(first=0, last=0)
        varC.set(0)
        varR.set(0)
        
        varL.set(' Выключено ')
        GPIO.output(pins, 0)        # LOW pin
        fl = 0
    print(' Нажата кнопка на пине ' + str(channel), 'flag = ', fl)
# ================================================ Инициализация GPIO
GPIO.setmode(GPIO.BCM)
FREQUENCY = 200				        # частота импульсов в Гц
pins = 19                           # подключение пина
pinb = 26
fl = 0                              # флаг изменения сотояния при нажатии кнопки
GPIO.setup(pins, GPIO.OUT)          # включение пина в режим OUTPUT
GPIO.setup(pinb, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
pwm = GPIO.PWM(pins, FREQUENCY)     # создаем ШИМ-объект для пина pins

print(' Ожидание нажатия кнопки ...')
GPIO.add_event_detect(pinb, GPIO.RISING, callback=func8, bouncetime=400)
# ================================================ Цикл Tkinter
root=Tk()
root.title('ПЗ 3/12. Использование библиотеки Tkinter.')
# геометрические параметры: ширина=500, высота=400; расположение  x=300, y=200
root.geometry('460x440+300+100') 
# ------------------------------------------------ обработчик закрытия окна
root.protocol('WM_DELETE_WINDOW', window_deleted) 
# --------------------------------- размер окна может быть изменён только по горизонтали
root.resizable(False, False) 
# ++++++++++++++++++++++++++++++++++++++++++++++++ Включение/выключение светодиода
Label(text="Включение/выключение светодиода").grid(row=0, column=0, columnspan=5, sticky=W+E, pady=10, padx=10)
# 1.---------------------------------------------- Entry
Label(text=" 1. Использование Entry: ").grid(row=1, column=0, columnspan=2, sticky=W)
varE = StringVar(root, value=' Выключить')
entry1 = Entry(root, text=varE, width=12) 
entry1.config(state='normal')     # 'disabled' 'normal' или 'readonly'
#entry1.config(bg='red')
#entry1.insert(0,' Выключить')
entry1.grid(row=1, column=3, sticky=W)
Button(text=" Ввод ", width=10, command=func1).grid(row=1, column=4, sticky=W)
#print(entry1.get())
# 2.---------------------------------------------- Spinbox
Label(text=" 2. Использование Spinbox: ").grid(row=2, column=0, columnspan=2, sticky=W)
varSp = StringVar(value=' Выключить')
spinbox1 = Spinbox(root, textvariable=varSp, width=12, from_=1, to=2, wrap=True, command=func2)
spinbox1.configure(values=(' Выключить', ' Включить'))
#spinbox1.configure(textvariable=var0)
spinbox1.grid(row=2, column=3, sticky=W)
# 3.---------------------------------------------- Listbox
Label(text=" 3. Использование Listbox: ").grid(row=3, column=0, columnspan=2, sticky=W)
var_default = [" Включить ", " Выключить "]
list_var = StringVar(value=var_default)
listbox1=Listbox(height=2, width=12, selectmode=SINGLE, listvariable=list_var, highlightcolor = 'red')
listbox1.grid(row=3, column=3, sticky=W)

#for options in listbox1.config():
#    print(options + ": " + str(listbox1[options]))
    
Button(text=" Ввод ", width=10, command=func3).grid(row=3, column=4, sticky=W)
# 4.---------------------------------------------- Checkbutton
Label(text=" 4. Использование Checkbutton:").grid(row=4, column=0, columnspan=2, sticky=W)
varC=IntVar() 
check1=Checkbutton(text=u' Вкл/Выкл ', variable=varC, onvalue=1, offvalue=0, command=func4) 
check1.grid(row=4, column=3, sticky=W)
# 5.---------------------------------------------- Button
Label(text=" 5. Использование Button: ").grid(row=5, column=0, columnspan=2, sticky=W)
Button(text=" Включить ", width=10, command=func51).grid(row=5, column=3, sticky=W)
Button(text=" Выключить ", width=10, command=func50).grid(row=5, column=4, sticky=W)
# 6.---------------------------------------------- Radiobutton
Label(text=" 6. Использование Radiobutton:").grid(row=6, column=0, columnspan=2, sticky=W)
varR=IntVar() 
rbutton1=Radiobutton(text='Включить',  variable=varR, value=1, command=func6) 
rbutton2=Radiobutton(text='Выключить ', variable=varR, value=0, command=func6) 
rbutton1.grid(row=6, column=3, sticky=W)
rbutton2.grid(row=6, column=4, sticky=W)

# ++++++++++++++++++++++++++++++++++++++++++++++++ Изменение яркости светодиода
Label(text="Изменение яркости светодиода").grid(row=7, column=0, columnspan=5, sticky=W+E, pady=10, padx=10)
# 7.---------------------------------------------- Listbox
Label(text=" 7. Использование Scale: ").grid(row=8, column=0, columnspan=2, sticky=W)
varS = IntVar()         # переменная только с целочисленными значениями
varS.set(50)            # установить значение по умолчанию 50
scale1 = Scale(label='Яркость в %', orient=HORIZONTAL, length=410, from_=0, to=100, variable=varS, tickinterval=10, resolution=1, command=func7)
scale1.grid(row=9, column=0, columnspan=7, sticky=W, padx=20)
# ++++++++++++++++++++++++++++++++++++++++++++++++ Использование кнопки
Label(text="Использование кнопки").grid(row=10, column=0, columnspan=5, sticky=W+E, pady=10, padx=10)
# 8.---------------------------------------------- Listbox
Label(text=" 8. Использование кнопки: ").grid(row=11, column=0, columnspan=2, sticky=W)
varL = IntVar()         # переменная только с целочисленными значениями
varL.set(' Выключено ') # установить значение выключено
label1 = Label(textvariable=varL, font=("Arial", 16), borderwidth=2, relief="ridge")
label1.grid(row=11, column=3, columnspan=2, sticky=W+E)

root.mainloop()
