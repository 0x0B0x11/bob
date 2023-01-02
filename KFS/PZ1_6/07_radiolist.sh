#!/bin/bash
DISTROS=$(whiptail --title  "Test Checklist Dialog" --checklist \
"What is the Linux distro of your choice?" 15 60 4 \
"debian" "Venerable Debian" ON \
"ubuntu" "Popular Ubuntu" OFF \
"fedora" "Stable CentOS" OFF \
"centOS" "Rising Star Mint" OFF 3>&1 1>&2 2>&3)
 
exitstatus=$?
if [ $exitstatus = 0 ];  then
     echo "The chosen distro is:" $DISTROS
else
     echo "You chose Cancel."
fi