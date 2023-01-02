#!/bin/bash
# ============================================= Подключение функций для внешних светодиодов
. /home/pi/KFS/lib/lib02_led/exportPin
. /home/pi/KFS/lib/lib02_led/setDirect
. /home/pi/KFS/lib/lib02_led/setState
. /home/pi/KFS/lib/lib02_led/unexportPin
. /home/pi/KFS/lib/lib02_led/readGPIO
# ============================================= Инициализация переменных
BASE_GPIO_PATH=/sys/class/gpio
TX=19		# Tx подключен к 19 пину
fl=0

# Присвоение названия состояниям
ON=1
OFF=0
# ============================================= Обработчик Ctrl-C для чистого завершения работы
shutdownKP() {
	echo " - это прерывание"
	read -p "Вы желаете прервать программу? y: " -n 1 answer; echo  
	if [ $answer == 'y' ];  then
		setState $TX $OFF
		unexportPin $TX
		
		echo "  Поки, споки!"
		exit 0
	fi
}
trap 'shutdownKP' SIGINT

# ============================================================= Основная программа
exportPin $TX
sleep 0.1
setDirect $TX "out"						# указание направление пину TX
setState $TX $ON						# установка "1" для TX для инициализации
sleep 5
while [ 1 ]								# бесконечный цикл, пока не нажато Ctrl-C
do
	read -n 1 symb
	z=$(ascii -t $symb)
	echo $z
	count=1
	for var in $z
	do
		if [ $count -eq 5 ];  then
			cod=$var
			echo $cod
		fi
		count=$(( $count + 1 ))
	done
	setState $TX $OFF; sleep 0.1		# стартовая посылка
	for (( i=7; i >= 0; i-- ))
	do
		echo ${cod:i:1}
		setState $TX ${cod:i:1}; sleep 0.1	# установка состояния в соответствии с кодом
	done
	setState $TX $ON; sleep 0.1			# стоповая посылка
done