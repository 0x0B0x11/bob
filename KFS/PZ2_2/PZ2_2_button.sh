#!/bin/bash
# Программа запускается без аргументов
# 
# Общий путь для доступа к GPIO
BASE_GPIO_PATH=/sys/class/gpio

# Присвоение имен номерам контактов GPIO для каждого цвета
RED=19
BOTTON=26

# Инициализация переменных
rG=1
z1=1
z=0		#  Инициализация переменной задержки свечения
fl=1	#  Инициализация флага переключения

# Присвоение названия состояниям
ON="1"
OFF="0"

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
    setLightState $RED $OFF
    unexportPin $RED
    unexportPin $BOTTON
    echo "  Поки, споки!"
    exit 0
  fi
}

trap shutdown SIGINT

# Экспорт пинов для их дальнейшего использования
exportPin $RED
exportPin $BOTTON
sleep 0.1
# Установка режима пина "выход"
setOutput $RED

# Установка режима пина "вход"
setInput $BOTTON

# Выключение света для инициализации
setLightState $RED $OFF

# Бесконечный цикл, пока не нажато Ctrl-C
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
	setLightState $RED $ON			# Красный светится
	else 
	setLightState $RED $OFF			# Красный гаснет	
  fi

done
