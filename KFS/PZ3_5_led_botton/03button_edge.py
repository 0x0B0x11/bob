#!/bin/python3
import RPi.GPIO as GPIO
from time import sleep
pin = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    print('Waiting for IO12 state cahnges ...')
#    GPIO.wait_for_edge(pin, GPIO.FALLING)
    GPIO.wait_for_edge(pin, GPIO.RISING)
    print('State change detected.')
except KeyboardInterrupt:
    print(" - это прерывание")
finally: 
    GPIO.cleanup(); print("Программа завершена")     
