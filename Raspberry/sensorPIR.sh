#!/usr/bin/python3
import subprocess
import time
import pygame
import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO_PIR = 7
GPIO.setup(GPIO_PIR,GPIO.IN)

dirOn27 = f"sudo /./home/julian/on27.sh" #LUZ AMARILLA
dirOff27 = f"sudo /./home/julian/off27.sh" #LUZ AMARILLA
dirtimbreON = f"sudo /./home/julian/timbreON.sh" #TIMBRE
dirtimbreOFF = f"sudo /./home/julian/timbreOFF.sh" #TIMBRE

num=0
status0 = 0
status1 = 0
try :
    
    while True:
              status0 = 0
              print ("Listo para comenzar!")
              while True:
                        status0 = GPIO.input(GPIO_PIR)
                        if status0==1 and status1==0:
                                     num=num+1
                                     print ("Atencion se ha detectado movimiento ",num,"")
                                     status1=1
                                     os.system(dirOff27)
                                     os.system(dirtimbreOFF)
                        elif status0==0 and status1==1:
                                     print ("Listo para comenzar!")
                                     os.system(dirOn27)
                                     os.system(dirtimbreON)
                                     status1=0
                                     time.sleep(0.01)
except KeyboardInterrupt:
       GPIO.cleanup()

