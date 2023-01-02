#!/bin/bash
function myfunc {
read -p "Enter a value: " value
echo "adding value"
return $(( $value + 10 ))
}
myfunc
echo "The new value is $?"
#echo "The new value is $(myfunc)"
#. factorial
factorial 5
echo $?