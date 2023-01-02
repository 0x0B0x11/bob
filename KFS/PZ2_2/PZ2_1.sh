#!/bin/bash
# Программа запускается без аргументов
# 
# Общий путь для доступа к GPIO
BASE_GPIO_PATH=/sys/class/gpio

# Присвоение имен номерам контактов GPIO для каждого цвета
RED=13
YELLOW=6
GREEN=19
BOTTON=26

# Присвоение названия состояниям
ON="1"
OFF="0"

# Инициализация переменных
rG=1
z1=1
z=0			#  Инициализация переменной задержки свечения
fl=1		#  Инициализация флага переключения
fl_LED=1	#  Инициализация флага свечения

# Функция для экспорта пина, если он еще не экспортирован
exportPin()
{
  if [ ! -e $BASE_GPIO_PATH/gpio$1 ]; then
	echo "GPIO $1 экспортирован"
    echo "$1" > $BASE_GPIO_PATH/export
  fi
}
# Функция для прекращения экспорта пина, если он еще экспортирован
unexportPin()
{
  if [ -e $BASE_GPIO_PATH/gpio$1 ]; then
	echo "GPIO $1 unexport"
    echo "$1" > $BASE_GPIO_PATH/unexport
  fi
}

# Функция для установки пина в качестве выхода
setOutput()
{
  echo "out" > $BASE_GPIO_PATH/gpio$1/direction
}

# Функция для установки пина в качестве входа
setInput()
{
  echo "in" > $BASE_GPIO_PATH/gpio$1/direction
}

# Функция для изменения вкл/выкл светодиода
setLightState()
{
  echo $2 > $BASE_GPIO_PATH/gpio$1/value
}

# Функция для выключения всех светодиодов
allLightsOff()
{
  setLightState $RED $OFF
  setLightState $YELLOW $OFF
  setLightState $GREEN $OFF
}

# Функция для включения всех светодиодов
allLightsOn()
{
  setLightState $RED $ON
  setLightState $YELLOW $ON
  setLightState $GREEN $ON
}

# Функция чтения из порта GPIO в переменную rG
readGPIO()
{
  rG=$(cat $BASE_GPIO_PATH/gpio$1/value)
}

# Обработчик Ctrl-C для чистого завершения работы
shutdown()
{
  echo " - это прерывание"
  read -p "Вы желаете прервать программу? y: " answer
  if [ $answer == 'y' ];  then
    allLightsOff
    unexportPin $RED
    unexportPin $YELLOW
    unexportPin $GREEN
    unexportPin $BOTTON
  
    echo "  Поки, споки!"
    exit 0
  fi
}

trap shutdown SIGINT

# Экспорт пинов для их дальнейшего использования
exportPin $RED
exportPin $YELLOW
exportPin $GREEN
exportPin $BOTTON

# Установка режима пинов "выход"
setOutput $RED
setOutput $YELLOW
setOutput $GREEN

# Установка режима пина "вход"
setInput $BOTTON

# Выключение света для инициализации
allLightsOff
# Максимальное время свечения светодиодов
z1=1
z=0		#  Инициализация переменной задержки свечения
fl=1	#  Инициализация флага переключения
# Бесконечный цикл, пока не нажато Ctrl-C
while [ 1 ]
do
	#let "z++"
	z=$(bc <<< "($z % 5)+1")
	if [ $z -eq 1 ];  then
		fl=$(bc <<< "($fl+1) % 2")
		echo " Флаг fl = $fl !"
	fi
	if [ $fl -eq 0 ];  then
		z1=$(bc <<< "scale=4; $z1/2")
		echo "  z1 = $z1"
	else
		z1=$(bc <<< "scale=4; $z1*2")	
		echo "  z1 = $z1"
	fi
	# Проверяем кнопку
	rG1=$rG
	#sleep 0.1									# Ждем 0.1 секунды
	readGPIO $BOTTON
	if [[ "$rG1" -eq 1 ]] && [[ "$rG" -eq 0 ]];  then	# если нажата кнопка
		fl_LED=$(bc <<< "($fl_LED+1) % 2")				# смена состояния флага свечения
		echo "--------------------------- Flag_LED = $fl_LED"
	fi

	echo "  ---------------- z = $z"
	#объявляем цикл for
	for ((i=0; i<2; i++))
	do
		for ((j=0; j<2; j++))
		do
			for ((k=0; k<2; k++))
			do
				if [[ "$fl_LED" -eq 0 ]];  then
					setLightState $RED $i		# Красный
					setLightState $YELLOW $j	# Желтый
					setLightState $GREEN $k		# Зеленый
					else 
					setLightState $RED $k		# Красный
					setLightState $YELLOW $k	# Желтый
					setLightState $GREEN $k		# Зеленый
				fi
				sleep $z1						# Ждем 
			done
		done
	done
done
