#!/bin/bash
echo 539 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio539/direction
echo 1 > /sys/class/gpio/gpio539/value

