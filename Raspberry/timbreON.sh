#!/usr/bin/bash
echo 516 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio516/direction
echo 1 > /sys/class/gpio/gpio516/value


