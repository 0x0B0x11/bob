BASE_GPIO_PATH=/sys/class/gpio

exportPin()

{

if [ ! -e $BASE_GPIO_PATH/gpio$1 ]; then

echo "GPIO $1 экспортирован"

echo "$1" > $BASE_GPIO_PATH/export

sleep 0.2

fi

}

install_led(){

echo none > /sys/class/leds/led1/trigger

}

install_led

for (( i = 1; i <= 10; i++))

do

START_TIME=$(date +%s%3N)

for (( j = 1; j <= 1000; j++))

do

echo 1 > /sys/class/leds/led1/brightness

echo 0 > /sys/class/leds/led1/brightness

done

END_TIME=$(date +%s%3N)

DIFF=$(( $END_TIME - $START_TIME ))

echo $DIFF

echo $DIFF >> data.txt

done

echo input > /sys/class/leds/led1/trigger

cat data.txt;
