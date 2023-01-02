#!/bin/python3
import RPi.GPIO as GPIO
import time

#GPIO_PWM_0 = 27				# подключаем светодиод к порту 12
#GPIO_PWM_1 = 13				# подключаем светодиод к порту 13
#WORK_TIME = 3				# время работы 10 секунд
#DUTY_CYCLE = 50				# скважность
#FREQUENCY = 1				# частота меандра в Гц
#GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOAD)		# нумерация пинов как на плате
#GPIO.setup(GPIO_PWM_0, GPIO.OUT)	# определяем порты как output
#GPIO.setup(GPIO_PWM_1, GPIO.OUT)
#pwmOutput_0 = GPIO.PWM(GPIO_PWM_0, FREQUENCY)
#pwmOutput_1 = GPIO.PWM(GPIO_PWM_1, 2 * FREQUENCY)
#pwmOutput_0.start(DUTY_CYCLE)
#pwmOutput_1.start(DUTY_CYCLE)

#time.sleep(WORK_TIME)
#pwmOutput_0.stop()
#pwmOutput_1.stop()
#GPIO.cleanup()

#  ------------------------------------------------
GPIO_PWM_0 = 19
FREQUENCY = 300
DELAY_TIME = 0.1

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PWM_0, GPIO.OUT)

pwmOutput_0 = GPIO.PWM(GPIO_PWM_0, FREQUENCY)
pwmOutput_0.start(0)

try:
    while True:
        for dutyCycle in range(0, 51, 1):
            pwmOutput_0.ChangeDutyCycle(dutyCycle)
            time.sleep(DELAY_TIME)
except KeyboardInterrupt:
    pwmOutput_0.stop()
    GPIO.cleanup()
    print("  Успешное завершение!")

