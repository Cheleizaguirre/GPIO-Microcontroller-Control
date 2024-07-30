#!/bin/bash
echo 529 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio529/direction
echo 1 > /sys/class/gpio/gpio529/value

#Algo que puede cambiarse en el futuro
echo 0 > /home/julian/estado.txt


