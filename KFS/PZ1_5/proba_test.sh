#!/bin/bash 
val1="atext" 
val2="zanother text" 
if [ $val1 \> "$val2" ] 
then 
echo "$val1 is greater than $val2" 
else 
echo "$val1 is less than $val2"
fi
echo "Длина строки $val1 равна ${#val1}"
