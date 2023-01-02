#!/bin/bash 
trap '	echo " Trapped Ctrl-C "
		pwd'  			SIGINT
echo This is a test script 
count=1 
while [ $count -le 10 ] 
do 
	echo "Loop #$count" 
	sleep 1 
	count=$(( $count + 1 )) 
done
