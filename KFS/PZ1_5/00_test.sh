#!/bin/bash
# Определение числа строк в файле
IFS=$'\n'
if [ -e $1 ]; then
	n=`wc -l < $1`
	echo -e "\033[31m Число строк в файле $1 равно $n \033[0m" 
	if [[ $2 -ge 1 && $3 -ge 1 && $2 -le $n && $3 -le $n ]]; then
		counter=1 
		str=0
		max_count=0
		for var in $(cat $1)
		do 
			if [[ $counter -ge $2 && $counter -le $3 || $counter -ge $3 && $counter -le $2 ]]; then 
				echo "Строка №$counter:  $var "
				if [ ${#var} -gt $str ]; then 
					max_count=$counter
					str=${#var}
				fi
			fi
			counter=$(($counter + 1))
		done
		echo -e "\033[35m Строка максимальной длины ($str симв.) имеет номер $max_count"
	else echo " 1-й или 2-й аргументы выходят за границы диапазона "
	fi
else echo -e "\033[0m Файл\033[31m $1\033[0m не существует" 
fi
