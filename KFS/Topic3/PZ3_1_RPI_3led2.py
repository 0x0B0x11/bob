#!/bin/python3

import RPi.GPIO as GPIO             # импорт библиотеки GPIO
import time                         # импорт библиотеки временных функций
import sys, traceback               # импорт библиотеки для обработки исключений

try:
    print(GPIO.RPI_INFO)            # Информация об устройстве
    print(GPIO.VERSION)             # Информация о версии библиотеки
    print(GPIO.RPI_REVISION)        # Информация о коррекциях библиотеки
    GPIO.setmode(GPIO.BOARD)        # запусr GPIO

    # теперь Python знает о GPIO, и ему можно указать на то, с каким портом нужно будет работать и что он должен делать (в данном случае – 11-м и он будет работать на выход)
    pins=[31,33,35]
    GPIO.setup(pins, GPIO.OUT)
    tt=0.5                          # время в секундах
    for i in range(10):
        values=[1,1,0]
        GPIO.output(pins, values)   # далее включим лампочку на 5 секунд (11 – номер порта, а 1 – значит true)
        time.sleep(tt)
        values=[0,0,1]
        GPIO.output(pins, values)   # теперь выключим (0 – значит false)
        time.sleep(tt)
except KeyboardInterrupt:
    # ...
    print(" - Выход по нажатию Ctrl+C")    # выход из программы по нажатию Ctrl+C
except:
    # ...
    print("Опссс!... Что-то пошло не так") # прочие исключения
finally:
    print("Пины инициализированы")  # информируем сбросе пинов
    GPIO.cleanup()                  # возвращаем пины в исходное состояние
    print("Успешное завершение")    # информируем о завершении работы программы