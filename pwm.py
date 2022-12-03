import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT)

pwm = GPIO.PWM(26, 60)

pwm.start(0)

try:
  while True:
    for dutyCycle in range (0, 100, 5):
      pwm.ChangeDutyCycle(dutyCycle)
      time.sleep(0.1)

    for dutyCycle in range (100, 0, -5):
      pwm.ChangeDutyCycle(dutyCycle)
      time.sleep(0.1)

except KeyboardInterrupt:
  pwm.stop()

GPIO.cleanup()