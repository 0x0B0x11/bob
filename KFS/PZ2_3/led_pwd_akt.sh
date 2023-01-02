#!/bin/bash
# Программа запускается без аргументов
# 
BASE_GPIO_PATH=/sys/class/gpio
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
ON="1"
OFF="0"

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
shutdown2() {				# для выхода с использованием клавиши y
  echo " - это прерывание"
  read -p "Вы желаете прервать программу? y: " -n 1 answer; echo  
  if [ $answer == 'y' ];  then
		echo " - останов!"
		triggerVar $PWR $IN
		triggerVar $ACT $MM
		echo "  Поки, споки!"
		exit 0
  fi
  echo "Вы выбрали символ, отличный от y"
  return 0
}

trap shutdown SIGINT		# Перехват прерывания Ctrl-C (shutdown - для выхода с использованием whiptail)
# ------------------------------------------ Основная программа
# Экспорт пинов для их дальнейшего использования
triggerVar $ACT $GP
triggerVar $PWR $GP
while [ 1 ]
do
	setLightState $PWR $ON			# PWR светится
	setLightState $ACT $OFF			# ACT гаснет	
	sleep 0.5						# Ждем 0.5 секунды
	setLightState $ACT $ON			# ACT светится	
	setLightState $PWR $OFF			# PWR гаснет	
	sleep 0.5						# Ждем 0.5 секунды
done
