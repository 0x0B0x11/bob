#!/bin/bash

	read -t 3 -n 1 name; echo  
	echo " name = $name"
	
	if [ $name ];  then
		if [ $name == 'm' ]; then
			echo "Переменная $name существует"
		else
			echo "Переменная $name не существует"
		fi
	fi
