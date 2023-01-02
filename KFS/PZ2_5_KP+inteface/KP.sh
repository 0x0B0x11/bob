#!/bin/bash
# Программа запускается без аргументов
# ============================================= Подключение функций для внешних светодиодов
. /home/pi/KFS/lib/lib02_led/exportPin
. /home/pi/KFS/lib/lib02_led/setDirect
. /home/pi/KFS/lib/lib02_led/setState
. /home/pi/KFS/lib/lib02_led/unexportPin
. /home/pi/KFS/lib/lib02_led/readGPIO

# ============================================= Подключение функций для внутрених светодиодов
# --------------------- Инициализация переменных + загрузка фунций triggerVar() и setLightState()
# для обоих фунций 1-й аргумент - номер светодиода (1-PWD, 0-AKT)
# 2-й аргумент: для triggerVar() - в какой режим переводим: "gpio", "input", "mmc0"
# 				для setLightState() - вкл/выкл: "ON", "OFF"
# --- Функция shutdown() без аргументов для возвращения встроенных светодиодов в исходное состояние
. /home/pi/KFS/lib/lib01_led_board/init_ledBoard.lib
# ============================================= Инициализация переменных
BASE_GPIO_PATH=/sys/class/gpio
YELLOW=19		# желтый светодиод подключен к 19 пину
BOTTON=26		# кнопка подключена к 26 пину
rG=1			# переменная для хранения состояния кнопки
fl=1			#  флаг переключения свечения
flmode=0		#  флаг переключения режима ("0" - светодиоды ACT и PWD; "1" - внешние светодиоды)
# Присвоение названия состояниям
ON=1
OFF=0
# ============================================= Обработчик Ctrl-C для чистого завершения работы
shutdownKP() {
	echo " - это прерывание"
	read -p "Вы желаете прервать программу? y: " -n 1 answer; echo  
	if [ $answer == 'y' ];  then
		setState $YELLOW $OFF
		unexportPin $YELLOW
		unexportPin $BOTTON
		triggerVar $PWR $IN
		triggerVar $ACT $MM
		
		echo "  Поки, споки!"
		exit 0
	fi
	echo "Нажата клавиша, отличная от y"
	if [[ $flmode -eq 1 ]]; then
		if [[ $fl -eq 1 ]]; then
			echo "--------------------------- Выключено"
		else
			echo -e "\033[33m--------------------------- Включено!\033[0m"
		fi
	else
		if [[ $fl -eq 1 ]]; then
			echo -e "\033[42m\033[32m---------------------------\033[40m\033[32m Зелёный\033[0m"
		else
			echo -e "\033[41m\033[31m---------------------------\033[40m\033[31m Красный\033[0m"
		fi	
	fi
}
trap 'shutdownKP' SIGINT

# ============================================================= Основная программа
# --------------------------------- Экспорт пинов для их дальнейшего использования
triggerVar $ACT $GP
triggerVar $PWR $GP

exportPin $YELLOW
exportPin $BOTTON
sleep 0.1
setDirect $YELLOW "out"				# указание направление пину YELLOW
setDirect $BOTTON "in"				# указание направление пину BOTTON
setState $YELLOW $OFF				# выключение света для инициализации

echo -e "Выбран режим переключения светодиодов \033[32mACT\033[0m и \033[31mPWD\033[0m"

while [ 1 ]							# бесконечный цикл, пока не нажато Ctrl-C
do
	# ------------------------------ Отслеживание нажатия кнопки и переключения флага fl
	rG1=$rG
	sleep 0.05							# ждем 0.1 секунды
	readGPIO $BOTTON
	rG=$?
	if [[ "$rG1" -eq 1 ]] && [[ "$rG" -eq 0 ]];  then
		fl=$(bc <<< "($fl+1) % 2")		# смена состояния флага
		if [[ $fl -eq 1 ]]; then
			if [[ $flmode -eq 1 ]]; then
				echo "--------------------------- Выключено"
			else
				echo -e "\033[42m\033[32m---------------------------\033[40m\033[32m Зелёный\033[0m"
			fi
		else
			if [[ $flmode -eq 1 ]]; then
				echo -e "\033[33m--------------------------- Включено!\033[0m"
			else
				echo -e "\033[41m\033[31m---------------------------\033[40m\033[31m Красный\033[0m"
			fi
		fi
	fi
	# ------------------------------ Вкл/выкл светодиодов в зависимости от флага flmode
	if [[ $flmode -eq 1 ]]; then
		if [[ "$fl" -eq 0 ]];  then
			setState $YELLOW $ON			# Желтый светится
		else 
			setState $YELLOW $OFF			# Желтый гаснет	
		fi
	else
		if [[ "$fl" -eq 0 ]];  then
			setLightState $PWR $ON			# PWR светится
			setLightState $ACT $OFF			# ACT гаснет	
		else 
			setLightState $ACT $ON			# ACT светится	
			setLightState $PWR $OFF			# PWR гаснет	
		fi
	fi
	# ------------------------------ Отслеживание нажатия клавиши "m" и переключение режима работы
	read -t 0.001 -n 1 name
	if [ $name ];  then
		if [ $name == 'm' ]; then
			printf "\b  \n"					# затереть введенный символ
			setLightState $PWR $OFF			# PWR гаснет
			setLightState $ACT $OFF			# ACT гаснет	
			setState $YELLOW $OFF			# Желтый гаснет	
			
			OPTION=$(whiptail --title "Выбор режима" --menu "Выберете режим работы:" 15 60 2 \
			"1" "Переключение светодиодов ACT (зеленый) и PWD (красный)" \
			"2" "Включение и выключение внешнего светодиода" 3>&1 1>&2 2>&3)
			exitstatus=$?
			if [ $exitstatus = 0 ]; then
				if [[ "$OPTION" -eq 1 ]];  then
					echo -e "Выбран режим переключения светодиодов \033[32mACT\033[0m и \033[31mPWD\033[0m"
					flmode=0
				else
					echo -e "Выбран режим вкл/выкл \033[33mвнешнего светодиода\033[0m"
					flmode=1				
				fi
			fi
		else
			printf "\b  \n"					# затереть введенный символ
		fi
	fi

done
