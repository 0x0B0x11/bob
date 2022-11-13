#!/bin/bash

i=0

while read -r line
do
  i=$((i+1))
  if [ $i -eq $1 ] || [ $i -eq $2 ] || [ $i -eq $3 ]
  then
  echo "$i $line" >&2
  else
  echo "$i $line" >> ./myfile.txt
  fi

done < ./file_text.txt
