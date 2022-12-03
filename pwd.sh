#!/bin/bash
. ./sys.sh

setOutput()
{
echo "out" > $BASE_GPIO_PATH/gpio$1/direction
}

setIn(){
echo "in" > $BASE_GPIO_PATH/gpio$1/direction
}

setLightState()
{
echo "$1" > $BASE_GPIO_PATH/gpio19/value
}

allLightsOff()
{
echo 0 > $BASE_GPIO_PATH/gpio19/value
}

unexportPin() 
{
if [ -e $BASE_GPIO_PATH/gpio$1 ]; then
echo "GPIO $1 удален"
echo "$1" > $BASE_GPIO_PATH/unexport
sleep 0.2
fi

}

trap shutdown SIGINT
shutdown()
{
echo " - это прерывание"
read -p "Вы желаете прервать программу? y: " answer
if [ $answer == "y" ]; then
allLightsOff
unexportPin "19"
unexportPin "26"
uninstall_led
echo " Поки, споки!"
exit 0
fi 
}

leds(){
exportPin "19"
exportPin "26"
setOutput "19"
setIn "26"
pred_z=0
while :
do
	read_value
	sleep 0.05
	if [ $(cat $BASE_GPIO_PATH/gpio26/value) != $pred_z ]; then
		if [ $led == "1" ]; then
			setLightState "0"
		else
			setLightState "1"
		fi
	fi
done
}
