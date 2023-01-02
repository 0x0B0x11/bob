#!/bin/bash
PET=$(whiptail --title  "Тестовое поле ввода в произвольной форме" --inputbox  "Как зовут вашего питомца?" 10 60 Рыжик 3>&1 1>&2 2>&3)
 
exitstatus=$?
if [ $exitstatus = 0 ];  then
     echo "Имя твоего питомца: $PET"
else
     echo "Вы выбрали Отменить."
fi
