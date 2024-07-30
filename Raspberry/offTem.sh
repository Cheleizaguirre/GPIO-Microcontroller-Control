#!/bin/bash
echo 534 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio534/direction
echo 0 > /sys/class/gpio/gpio534/value

#Algo que puede cambiarse en el futuro
echo 0 > /home/julian/estado.txt

echo 529 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio529/direction
echo 1 > /sys/class/gpio/gpio529/value


