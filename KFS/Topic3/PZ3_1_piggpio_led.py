#!/bin/python3
import pigpio
import time
ledPin = 27
pi = pigpio.pi()
pi.set_mode(ledPin, pigpio.OUTPUT)
while (True):
    pi.write(ledPin, True)
    time.sleep(1)
    pi.write(ledPin, False)
    time.sleep(1)
