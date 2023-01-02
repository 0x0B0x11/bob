#!/bin/bash
# Программа запускается без аргументов
# 
BASE_GPIO_PATH=/sys/class/gpio
YELLOW=19
BOTTON=26
# --------------- Инициализация переменных + загрузка фунций triggerVar() и setLightState()
# для обоих фунций 1-й аргумент - номер светодиода (1-PWD, 0-AKT)
# 2-й аргумент: для triggerVar() - в какой режим переводим: "gpio", "input", "mmc0"
# 				для setLightState() - вкл/выкл: "ON", "OFF"
# --- Функция shutdown() без аргументов для возвращения встроенных светодиодов в исходное состояние
. ./init_ledBoard.lib
# Инициализация переменных
rG=1
z1=1
z=0		#  Инициализация переменной задержки свечения
fl=1	#  Инициализация флага переключения

# Присвоение названия состояниям
ON=1
OFF=0

# --------------------------------------------- Функции для GPIO
# Функция подключения пина, если он еще не подключен (один аргумент: 1-й - номер пина)
exportPin() {
  if [ ! -e $BASE_GPIO_PATH/gpio$1 ]; then
	echo "GPIO $1 экспортирован"
    echo $1 > $BASE_GPIO_PATH/export
  fi
}

# Функция выбора режима (два аргумента: 1-й - номер пина; 2-й - режим работы: "in" или "out")
setDirect() {
sudo echo $2 > /sys/class/gpio/gpio$1/direction
}

# Функция подачи на пин напряжения (два аргумента: 1-й - номер пина, 2-й - состояние)
setState() {
echo $2 > /sys/class/gpio/gpio$1/value
}

# Функция отключения пина, если он еще подключен
unexportPin() {
  if [ -e $BASE_GPIO_PATH/gpio$1 ]; then
	echo "GPIO $1 unexport"
    echo "$1" > $BASE_GPIO_PATH/unexport
  fi
}

# Функция чтения из порта GPIO в переменную rG
readGPIO() {
  rG=$(cat $BASE_GPIO_PATH/gpio$1/value)
}
# Обработчик Ctrl-C для чистого завершения работы
shutdown1()
{
	echo " - это прерывание"
	read -p "Вы желаете прервать программу? y: " -n 1 answer; echo  
	if [ $answer == 'y' ];  then
		setState $YELLOW $OFF
		unexportPin $YELLOW
		unexportPin $BOTTON
		echo "  Поки, споки!"
		exit 0
	fi
	echo "Нажата клавиша, отличная от y"
	if [[ $fl -eq 1 ]]; then
		echo "--------------------------- Выключено"
	else
		echo "--------------------------- Включено!"
	fi
}

trap shutdown1 SIGINT

# ------------------------------------------ Основная программа
# Экспорт пинов для их дальнейшего использования
#triggerVar $ACT $GP
#triggerVar $PWR $GP
exportPin $YELLOW
exportPin $BOTTON
sleep 0.1
setDirect $YELLOW "out"				# указание направление пину YELLOW
setDirect $BOTTON "in"				# указание направление пину BOTTON
# Выключение света для инициализации
setState $YELLOW $OFF

# Бесконечный цикл, пока не нажато Ctrl-C
while [ 1 ]
do
	rG1=$rG
	sleep 0.1						# Ждем 0.1 секунды
	readGPIO $BOTTON
#	echo "$rG"
  if [[ "$rG1" -eq 1 ]] && [[ "$rG" -eq 0 ]];  then
	fl=$(bc <<< "($fl+1) % 2")		# смена состояния флага
	if [[ $fl -eq 1 ]]; then
		echo "--------------------------- Выключено"
	else
		echo "--------------------------- Включено!"
	fi
  fi
  
  if [[ "$fl" -eq 0 ]];  then
	setState $YELLOW $ON			# Желтый светится
	else 
	setState $YELLOW $OFF			# Желтый гаснет	
  fi
done
