#!/bin/bash
trap shutdown SIGINT		# Перехват прерывания Ctrl-C
shutdown()
{
  echo " - это прерывание"
  read -p "Вы желаете прервать программу? y: " answer
  if [ $answer == 'y' ];  then
    echo "  Поки, споки!"
    exit 0
  fi
}

for (( i=1; i <= 5; i++ ))
do
	#export TERM=linux
	if (whiptail --title "Пробуем блок Да/Нет" --yesno "Выберите между Да или Нет." 10 60) then
		z=$?
		#echo "Вы выбрали Да. Статус выхода был $?."
	else
		z=$?
		#echo "Вы выбрали нет. Статус выхода был $?."
	fi
	
	#sleep 1
	#echo " Итерация $i"

done

echo "Вы выбрали нет. Последний статус выхода был $z."
