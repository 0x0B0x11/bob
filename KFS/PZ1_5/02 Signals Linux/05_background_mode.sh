#!/bin/bash
count=1
while [ $count -le 10 ]
do
	echo " count = $count"
	sleep 1
	count=$(( $count + 1 ))
done