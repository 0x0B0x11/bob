#!/bin/python3
import RPi.GPIO as GPIO
import time
#  ------------------------------------------------
pin_PWM = 19				        # подключаем светодиод к порту 12
FREQUENCY = 200				    # частота меандра в Гц
flag = 0                            # флаг увеличения/уменьшения яркости
GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOAD)		    # нумерация пинов как на плате
GPIO.setup(pin_PWM, GPIO.OUT)	    # определяем порты как output
pin_Out = GPIO.PWM(pin_PWM, FREQUENCY)
DELAY_TIME = 0.1
pin_Out.start(0)
#  ------------------------------------------------
try:
    while True:
        if flag == 0:
            print('Увеличения яркости свечения')
            flag = 1
            for dutyCycle in range(0, 20, 1):
                pin_Out.ChangeDutyCycle(dutyCycle)
                time.sleep(DELAY_TIME)
        else:
            print('Уменьшения яркости свечения')
            flag = 0
            for dutyCycle in range(20, 0, -1):
                pin_Out.ChangeDutyCycle(dutyCycle)
                time.sleep(DELAY_TIME)

except KeyboardInterrupt:
    pin_Out.stop()
    GPIO.cleanup()
    print("  Успешное завершение!")
