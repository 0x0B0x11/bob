#!/bin/bash
result=$(pwd 3>&1 1>&2 2>&3)
#err=7
echo 3>&1 1>&2 2>&3 $result
#3>&1 1>&2 2>&3; echo $result
