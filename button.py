import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(21, GPIO.IN) 
while True: 
    if GPIO.input(21) == 1: 
        print("Button is pressed") 
        time.sleep(0.25)