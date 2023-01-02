#!/bin/python3
from gpiozero import LED
from time import sleep
led = LED(27)
while True:
    led.on()
    sleep(0.7)
    led.off()
    sleep(0.2)
