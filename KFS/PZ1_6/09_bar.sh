#!/bin/bash
{
     for ((i = 0 ; i <= 100 ; i+=1));  do
         sleep 0.05
         echo $i
     done
} | whiptail --gauge  "Please wait while installing" 6 60 2