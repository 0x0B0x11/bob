#!/bin/bash

fl=0
z=$(ascii -t 1)
echo $z
count=1
for var in $z
do
	if [ $count -eq 5 ];  then
		cod=$var
		echo $cod
	fi
	count=$(( $count + 1 ))
done
for (( i=7; i >= 0; i-- ))
do
	echo ${cod:i:1}
done