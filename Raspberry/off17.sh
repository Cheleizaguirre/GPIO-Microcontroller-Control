#!/bin/bash
echo 529 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio529/direction
echo 0 > /sys/class/gpio/gpio529/value

