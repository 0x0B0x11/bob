#!/bin/bash
source=$1
dest=11
if [[ "$source" -eq 11 ]]
then
echo "Приемние и источник равны"
exit 1
else
echo "Приемник и источник не равны"    
fi
exit 0
