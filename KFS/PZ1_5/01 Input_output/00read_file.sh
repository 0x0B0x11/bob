#!/bin/bash 
exec 0< ~/KFS/PZ1_5/proba_test.sh 
count=1 
while read line 
do 
echo "Line #$count: $line" 
count=$(( $count + 1 )) 
done