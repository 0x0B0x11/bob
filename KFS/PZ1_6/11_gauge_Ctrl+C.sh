#!/usr/bin/env bash

for i in {1..100}; do
   sleep 0.1
   export TERM=linux
   echo $i | whiptail --gauge "Doing something" 10 50 $i
done
