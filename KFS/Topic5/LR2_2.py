#!/bin/python3
#  -------------------------------- Загрузка библиотек
import RPi.GPIO as GPIO
import time
import timeit
#  -------------------------------- Инициализация переменных
pinOut = 27                         # выходной пин
pinIn = 26                          # входной пин
DELAY_TIME = 1
fl = False                          # флаг для включения светодиодов
fl_print = False                    # флаг обработки результатов
x0 = 0.99999                        # инициализация x0    
x = 1                               # инициализация x    
N = 10                              # число умножений
n = 0                               # инициализация счетчика
n_repite = 0                        # инициализация числа тестов
n_t = 0                             # инициализация числа тестов

GPIO.setmode(GPIO.BCM)              # режим нумерации портов
GPIO.setup(pinOut, GPIO.OUT)        # установка pinOut в режим вывода
GPIO.setup(pinIn, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # установка pinIn в режим в вода с подтяжкой высокого уровня

code_to_test = """
x = x*x0
"""
#  -------------------------------- Текст программы потока 2
def test_callback(channel):
    global fl
    global fl_print
    global x
    global n
    fl = not fl
    if fl == False:
        fl_print = True
    else:
        x = 1                           #  инициализация x
        n = 0                           #  обнуление счетчика
    
    if fl == True:
        print('Кнопка нажата на пине № ' + str(channel))
        print('fl = ' + str(fl) + '; Тест запущен!')

GPIO.add_event_detect(pinIn, GPIO.FALLING, callback=test_callback, bouncetime=300)

#  -------------------------------- Текст программы потока 1
try:
    for i in range(N):
        x = x*x0
        print('x^' + str(i+1) + ' = ' + str(x))
        
    while True:
        if fl == True:
            time.sleep(DELAY_TIME)
            n_repite = n_repite + 1
#            GPIO.output(pinOut, GPIO.HIGH)
#            time.sleep(DELAY_TIME)
#            GPIO.output(pinOut, GPIO.LOW)
#            time.sleep(DELAY_TIME)
            
        if fl_print == True:                    # печать результатов
            for i in range(n_repite):
                elapsed_time = timeit.timeit(stmt=code_to_test, setup="x = 1; x0 = 0.99999", number=N)
                print('Время расчета ' + str(i+1) + '-й итерации = ' + str(elapsed_time))
                n_t = n_t + elapsed_time

            print('Среднее время расчета = ' + str(n_t/n_repite) + '; число повторов теста = ' + str(n_repite))
            print('fl = ' + str(fl) + '; Конец расчета')
            fl_print = False
            n_t = 0
            n_repite = 0
      
except KeyboardInterrupt:
    GPIO.cleanup()
    print("  Успешное завершение!")

