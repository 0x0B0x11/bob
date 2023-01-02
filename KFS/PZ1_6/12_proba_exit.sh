#!/bin/bash

for i in {1..100}; do
#   echo $i
   sleep 0.01
   read -t 1 -N 1 input
   
   if [[ $input == 'q' ]] || [[ $input == "Q" ]];then
		echo "Сработал break: i = $i"
        break;
   fi
done