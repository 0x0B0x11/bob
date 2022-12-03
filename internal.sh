#!/bin/bash
BASE_GPIO_PATH=/sys/class/gpio
exportPin()
{
if [ ! -e $BASE_GPIO_PATH/gpio$1 ]; then
echo "GPIO $1 экспортирован"
echo "$1" > $BASE_GPIO_PATH/export
sleep 0.2
fi
}

setOutput()
{
echo "out" > $BASE_GPIO_PATH/gpio$1/direction
}

setIn(){
echo "in" > $BASE_GPIO_PATH/gpio$1/direction
}

read_value(){
	btn=$(cat $BASE_GPIO_PATH/gpio26/value)
	led=$(cat $BASE_GPIO_PATH/gpio19/value)
}

setLightState()
{
echo "$1" > $BASE_GPIO_PATH/gpio19/value
}

allLightsOff()
{
echo "0" > $BASE_GPIO_PATH/gpio19/value
}

unexportPin() 
{
echo "1" > $BASE_GPIO_PATH/gpio19/unexport
}

trap shutdown SIGINT
shutdown()
{
echo " - это прерывание"
read -p "Вы желаете прервать программу? y: " answer
if [ $answer == "y" ]; then
allLightsOff
unexportPin $RED
unexportPin $BOTTON
echo " Поки, споки!"
exit 0
fi 
}


exportPin "19"
exportPin "26"
setOutput "19"
setIn "26"
pred_z=0
while :
do
	read_value
	sleep 0.12
	if [ $(cat $BASE_GPIO_PATH/gpio26/value) != $pred_z ]; then
		if [ $led == "1" ]; then
			setLightState "0"
		else 
			setLightState "1"	
		fi
	fi
	read -t 0.001 -n whip_flag
	if [ $whip_flag == "m" ]; then
		break
	fi
	echo $btn
done
