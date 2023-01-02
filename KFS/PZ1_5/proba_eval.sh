#!/bin/bash 
# Как работает команда eval
foo=10 x=foo
echo $x и еще '$' '5'
y='$'$x
echo $y
eval y='$'$x
echo $y
