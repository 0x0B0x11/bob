#!/bin/bash
. ./sys.sh
. ./external_leds.sh
. ./internal_leds.sh
while :
do
OPTION=$(whiptail --title "Пробуем меню" --menu "Сделайте
ваш выбор" 15 60 4 \
"1" "Системный светодиод" \
"2" "Внешний светодиод"  3>&1 1>&2 2>&3)
exitstatus=$?
if [ $OPTION = 1 ]; then
	internal
fi
if [ $OPTION = 2 ]; then
	external
fi
if [ $exitstatus != 0 ]; then
break
fi
done

