#!/bin/bash
var1=$(whiptail --title "Бокс с сообщением" --msgbox "Создаём информационный блок с whiptail. Нажмите Ok для продолжения." 10 60 3>&1 1>&2 2>&3)
echo $?
echo "$var1"
sleep 5