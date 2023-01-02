#!/bin/python3
import RPi.GPIO as GPIO
from time import sleep
pin = 26
GPIO.setmode(GPIO.BCM) 
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        if GPIO.input(pin):
            print('IOpin = HIGH')
        else:
            print('IOpin = LOW')
        sleep(0.1)
except KeyboardInterrupt:
    print(" - это прерывание")
finally: 
    GPIO.cleanup(); print("Программа завершена")     
