#!/bin/bash

IP=$(hostname -I)

function hex() {
  printf "0x%02x\n" "'$1"
}

for i in `echo $IP | grep -o .`;
  do
   hx=$(hex $i)
   i2cset -y 1 0x3e 0x40 $hx
  done
