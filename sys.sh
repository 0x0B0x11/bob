BASE_GPIO_PATH=/sys/class/gpio
exportPin()
{
if [ ! -e $BASE_GPIO_PATH/gpio$1 ]; then
echo "GPIO $1 экспортирован"
echo "$1" > $BASE_GPIO_PATH/export
sleep 0.2
fi
}

read_value(){
        btn=$(cat $BASE_GPIO_PATH/gpio26/value)
        led=$(cat $BASE_GPIO_PATH/gpio19/value)
	sysled=$(cat /sys/class/leds/led1/brightness)
}
