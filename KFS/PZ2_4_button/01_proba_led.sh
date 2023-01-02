#!/bin/bash
# Программа запускается без аргументов
# 
BASE_GPIO_PATH=/sys/class/gpio
YELLOW=19
BOTTON=26

echo $YELLOW > /sys/class/gpio/export
sleep 0.1
echo out > /sys/class/gpio/gpio$YELLOW/direction

echo 1 > /sys/class/gpio/gpio$YELLOW/value
sleep 1
echo 0 > /sys/class/gpio/gpio$YELLOW/value
sleep 1
echo 1 > /sys/class/gpio/gpio$YELLOW/value
sleep 1
echo 0 > /sys/class/gpio/gpio$YELLOW/value
sleep 1

echo 19 > /sys/class/gpio/unexport