import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
for i in range(5):
        GPIO.output(26, 1)
        time.sleep(2)
        GPIO.output(26,0)
        time.sleep(2)

GPIO.cleanup()