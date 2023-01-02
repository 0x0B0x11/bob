#!/bin/bash
# Программа запускается без аргументов
# 
# Общий путь для доступа к GPIO
BASE_LED_PATH=/sys/class/leds
BASE_GPIO_PATH=/sys/class/gpio

# Присвоение имен номерам контактов GPIO для каждого цвета
ACT=0
PWR=1
GP="gpio"
IN="input"
MM="mmc0"
BOTTON=26

# Инициализация переменных
rG=1
z1=1
z=0		#  Инициализация переменной задержки свечения
fl=1	#  Инициализация флага переключения

# Присвоение названия состояниям
ON="1"
OFF="0"
# -------------------------- Функции для встроенных светодиодов
# Функция переключения режимов встроенных светодиодов
triggerVar()
{
	echo "Режим $2 включен для led$1"
    echo $2 | sudo tee $BASE_LED_PATH/led$1/trigger
}
# Функция вкл/выкл светодиода
setLightState()
{
  echo $2 | sudo tee $BASE_LED_PATH/led$1/brightness
}

# --------------------------------------------- Функции для GPIO
# Функция подключения пина, если он еще не подключен
exportPin()
{
  if [ ! -e $BASE_GPIO_PATH/gpio$1 ]; then
	echo "GPIO $1 экспортирован"
    echo "$1" > $BASE_GPIO_PATH/export
  fi
}
# Функция отключения пина, если он еще подключен
unexportPin()
{
  if [ -e $BASE_GPIO_PATH/gpio$1 ]; then
	echo "GPIO $1 unexport"
    echo "$1" > $BASE_GPIO_PATH/unexport
  fi
}
# Функция установки пина в качестве входа
setInput()
{
  echo "in" > $BASE_GPIO_PATH/gpio$1/direction
}
# Функция чтения из порта GPIO в переменную rG
readGPIO()
{
  rG=$(cat $BASE_GPIO_PATH/gpio$1/value)
}

# -------------------------------------- Обработчик прерывания
# Обработчик Ctrl-C для чистого завершения работы
trap shutdown SIGINT		# Перехват прерывания Ctrl-C
shutdown()
{
  echo " - это прерывание"
  read -p "Вы желаете прервать программу? y: " answer
  if [ $answer == 'y' ];  then
    triggerVar $PWR $IN
    triggerVar $ACT $MM
    unexportPin $BOTTON
    echo "  Поки, споки!"
    exit 0
  fi
}

# ------------------------------------------ Основная программа
# Экспорт пинов для их дальнейшего использования
triggerVar $ACT $GP
triggerVar $PWR $GP
exportPin $BOTTON

# Установка режима пина "вход"
setInput $BOTTON

# --------------------- Бесконечный цикл, пока не нажато Ctrl-C
while [ 1 ]
do
	rG1=$rG
	sleep 0.1						# Ждем 0.1 секунды
	readGPIO $BOTTON
#	echo "$rG"
  if [[ "$rG1" -eq 1 ]] && [[ "$rG" -eq 0 ]];  then
	fl=$(bc <<< "($fl+1) % 2")		# смена состояния флага
	echo "--------------------------- Flag = $fl"
  fi
  
  if [[ "$fl" -eq 0 ]];  then
	setLightState $PWR $ON			# PWR светится
	setLightState $ACT $OFF			# ACT гаснет	
	else 
	setLightState $ACT $ON			# ACT светится	
	setLightState $PWR $OFF			# PWR гаснет	
  fi

done
