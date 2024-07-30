#!/bin/bash
while true
    do
        valor1=$(python3 read.py | grep "ON"  | cut -d " " -f3 | cut -b 24-25)
        valor2=$(python3 read.py | grep "OFF" | cut -d " " -f3  | cut -b 24-26)

        if [ $valor1 = 'ON' ]
        then
            echo $valor1
            sudo /./home/julian/off17.sh
            sudo /./home/julian/on22.sh
        else
            if [ $valor2 = 'OFF' ]
                 then
                    echo $valor2
                    sudo /./home/julian/off22.sh
                    sudo /./home/julian/on17.sh
                 fi
        fi
        sleep 1
        done