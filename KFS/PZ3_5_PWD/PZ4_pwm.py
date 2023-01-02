#!/bin/python3
import RPi.GPIO as GPIO
import time

GPIO_PWM_0 = 19				# подключаем светодиод к порту 12
#GPIO_PWM_1 = 13		    # подключаем светодиод к порту 13
WORK_TIME = 10				# время работы 10 секунд
DUTY_CYCLE = 50		        # 1/скважность
FREQUENCY = 200				# частота меандра в Гц
GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOAD)		# нумерация пинов как на плате
GPIO.setup(GPIO_PWM_0, GPIO.OUT)	# определяем порты как output
#GPIO.setup(GPIO_PWM_1, GPIO.OUT)
pwmOutput_0 = GPIO.PWM(GPIO_PWM_0, FREQUENCY)
#pwmOutput_1 = GPIO.PWM(GPIO_PWM_1, 2 * FREQUENCY)
pwmOutput_0.start(DUTY_CYCLE)
#pwmOutput_1.start(DUTY_CYCLE)
time.sleep(WORK_TIME)
pwmOutput_0.stop()
#pwmOutput_1.stop()
GPIO.cleanup()
print("Успешное завершение!")


