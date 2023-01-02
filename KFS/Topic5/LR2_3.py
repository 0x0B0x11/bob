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
N = 100                             # число умножений
n = 0                               # инициализация счетчика
n_repite = 0                        # инициализация числа тестов
n_t = 0                             # инициализация числа тестов

GPIO.setmode(GPIO.BCM)              # режим нумерации портов
GPIO.setup(pinIn, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # установка pinIn в режим в вода с подтяжкой высокого уровня

code_to_test = """
x = x*x0
"""
code_to_test2 = """
GPIO.output(pinOut, GPIO.HIGH)
# time.sleep(DELAY_TIME)
GPIO.output(pinOut, GPIO.LOW)
# time.sleep(DELAY_TIME)
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
    while True:
        if fl == True:                          # подсчет числа итераций теста
            time.sleep(DELAY_TIME)
            n_repite = n_repite + 1
        if fl_print == True:                    # печать результатов
            for i in range(n_repite):
                elapsed_time = timeit.timeit(stmt=code_to_test2, setup="\
import RPi.GPIO as GPIO;\
import time;\
DELAY_TIME = 0.2;\
pinOut = 27;\
GPIO.setmode(GPIO.BCM);\
GPIO.setup(pinOut, GPIO.OUT)\
", number=N)
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

