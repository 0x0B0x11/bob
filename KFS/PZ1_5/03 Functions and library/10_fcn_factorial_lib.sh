#!/bin/bash 
. ./09_lib_fcn_factorial
read -p "Enter value: " value 
result=$(factorial $value) 
echo "The factorial of $value is: $result" 
