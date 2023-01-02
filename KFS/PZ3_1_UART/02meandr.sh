#!/bin/bash
# Программа запускается без аргументов
# 
# Общий путь для доступа к GPIO
BASE_GPIO_PATH=/sys/class/gpio

# Присвоение имен номерам контактов GPIO для каждого цвета
BLUE=21

# Присвоение названия состояниям
ON="1"
OFF="0"

# Функция для экспорта пина, если он еще не экспортирован
exportPin() {
  if [ ! -e $BASE_GPIO_PATH/gpio$1 ]; then
	echo "GPIO $1 экспортирован"
    echo "$1" > $BASE_GPIO_PATH/export
  fi
}
# Функция для прекращения экспорта пина, если он еще экспортирован
unexportPin() {
  if [ -e $BASE_GPIO_PATH/gpio$1 ]; then
	echo "GPIO $1 unexport"
    echo "$1" > $BASE_GPIO_PATH/unexport
  fi
}
# Функция для установки пина в качестве выхода
setOutput() {
  echo "out" > $BASE_GPIO_PATH/gpio$1/direction
}
# Функция для установки пина в качестве входа
setInput() {
  echo "in" > $BASE_GPIO_PATH/gpio$1/direction
}
# Функция для изменения вкл/выкл светодиода
setLightState() {
  echo $2 > $BASE_GPIO_PATH/gpio$1/value
}

# Обработчик Ctrl-C для чистого завершения работы
shutdown()
{
  echo " - это прерывание"
  read -p "Вы желаете прервать программу? y: " answer
  if [ $answer == 'y' ];  then
	setLightState $BLUE $OFF	# Выключить сведодиод
    unexportPin $BLUE
    echo "  Поки, споки!"
    exit 0
  fi
}

trap shutdown SIGINT

# Экспорт пинов для их дальнейшего использования
exportPin $BLUE					# Экспорт пинов для их дальнейшего использования
sleep 0.1						# Ждем 0.1 секунды
setOutput $BLUE					# Установка режима пинов "выход"
setLightState $BLUE $OFF		# Выключение света для инициализации

# ----------------------------- Основная программа
while [ 1 ]						# Бесконечный цикл, пока не нажато Ctrl-C
do
	setLightState $BLUE $ON		# Выключить сведодиод
	sleep 0.0005					# Ждем 0.5 секунды
	setLightState $BLUE $OFF	# Выключить сведодиод
	sleep 0.0005					# Ждем 0.5 секунды
done
