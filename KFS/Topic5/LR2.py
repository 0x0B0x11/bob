#!/bin/python3
import RPi.GPIO as GPIO
import time

#  -------------------------------- Инициализация переменных
pinOut = 27                         # выходной пин
pinIn = 26                          # входной пин
DELAY_TIME = 0.3
fl = False                          # флаг для включения светодиодов
x0 = 2                              # 0.9991    
x = 1                               #  инициализация x

GPIO.setmode(GPIO.BCM)              # режим нумерации портов
GPIO.setup(pinOut, GPIO.OUT)        # установка pinOut в режим вывода
GPIO.setup(pinIn, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # установка pinIn в режим в вода с подтяжкой высокого уровня
#  -------------------------------- Текст программы потока 2
def test_callback(channel):
    global fl
    global x
    fl = not fl
    x = 1                           #  инициализация x
    
    print('Кнопка нажата на пине № ' + str(channel) + ';  fl = ' + str(fl))

GPIO.add_event_detect(pinIn, GPIO.FALLING, callback=test_callback, bouncetime=300)

#  -------------------------------- Текст программы потока 1
try:
    while True:
        if fl == True:
            for i in range(4):  # равносильно инструкции for i in 0, 1, 2, 3:
                # здесь можно выполнять циклические действия
                x = x*x0
                print('i = ' + str(i) + '; x = ' + str(x))
            print('fl = ' + str(fl))
            GPIO.output(pinOut, GPIO.HIGH)
            time.sleep(DELAY_TIME)
            GPIO.output(pinOut, GPIO.LOW)
            time.sleep(DELAY_TIME)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    print("  Успешное завершение!")

