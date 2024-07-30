#!/bin/bash
echo 534 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio534/direction
echo 1 > /sys/class/gpio/gpio534/value

#Algo que puede cambiarse en el futuro
echo 1 > /home/julian/estado.txt


