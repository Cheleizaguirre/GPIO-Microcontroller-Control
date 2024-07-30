#!/bin/bash
sudo sshpass -p "12345" ssh -l julian 192.168.100.40 'pkill -f lectura.sh'