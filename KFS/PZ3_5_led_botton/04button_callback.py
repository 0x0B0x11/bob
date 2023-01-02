#!/bin/python3
import RPi.GPIO as GPIO
from time import sleep
InputPin = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(InputPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def test_callback(channel):
    print('Кнопка нажата')

print('Ожидание изменения состояния InputPin ...')
GPIO.add_event_detect(InputPin, GPIO.FALLING, callback=test_callback)

try:
    while True:
        sleep(1)
        print('.')
except KeyboardInterrupt:
    print(" - это прерывание")
finally: 
    GPIO.cleanup(); print("Программа завершена")     
