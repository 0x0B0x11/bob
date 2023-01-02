#!/bin/python3
import RPi.GPIO as GPIO
from time import sleep
pin = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

x = 0

def callback_func_1(channel):
    print('Interupt on ' + str(channel))

def callback_func_2(channel):
    global x 
    x = x + 1

#GPIO.add_event_detect(pin, GPIO.FALLING)
GPIO.add_event_detect(pin, GPIO.FALLING, bouncetime=600)
GPIO.add_event_callback(pin, callback_func_1)
#GPIO.add_event_callback(pin, callback_func_2)

try:
    while True:
        sleep(1)
        print(str(x))
except KeyboardInterrupt:
    print(" - это прерывание")
finally: 
    GPIO.cleanup(); print("Программа завершена")     

