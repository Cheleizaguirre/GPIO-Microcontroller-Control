#!/bin/bash
echo 534 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio534/direction
echo 0 > /sys/class/gpio/gpio534/value
