#!/bin/bash 
# Управляющая конструкция if-then-else
user=anotherUser 
# user=pi 
folder=/home/pi/KFS/Lecture1_5
if grep $user /etc/passwd 
then 
echo " Пользователь $user существует " 
elif ls $folder 
then 
echo " Пользователь $user не существует, но есть каталог $folder " 
else
echo " Нет ни пользователя $user ни каталога $folder "
fi
