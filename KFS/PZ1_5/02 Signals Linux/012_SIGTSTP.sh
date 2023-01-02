#!/bin/bash 
#trap '	echo " Trapped Ctrl-Z "
#		pwd'  			SIGTSTP 
 
echo This is a test script 
count=1 
while [ $count -le 10 ] 
do 
	echo "Loop #$count" 
	sleep 50 
	count=$(( $count + 1 )) 
done