#!/bin/bash
# Программа запускается с одним аргументом: 11 - pwd светится
# 
# Общий путь для доступа к GPIO
PWD_PATH=/sys/class/leds/led1
source=$1
dest=11
echo gpio | sudo tee $PWD_PATH/trigger
if [[ "$source" -eq 11 ]]
then
echo "Светодиод PWR светится"
echo 1 | sudo tee $PWD_PATH/brightness
else
echo "Светодиод PWR погас"
echo 0 | sudo tee $PWD_PATH/brightness
fi
#echo input | sudo tee /sys/class/leds/led1/trigger
