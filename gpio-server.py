#!/usr/bin/python
# -*- coding: utf-8 -*-

# Echo server program
import socket
import os
import sys

sys.path.append("/home/pi/git/quick2wire-python-api")

import datetime
from time import sleep
from quick2wire.gpio import pins, Out
from itertools import cycle

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

led = pins.pin(5, direction = Out)
led_state = 1

def ledon():
        print('In led on')    
        led.value=1
        #sleep(30)

def ledoff():
        led.value=0

s.bind((HOST, PORT))
s.listen(1)

with led:
    while True:
        conn, addr = s.accept()
        print('Connected by', addr)
        data = conn.recv(1024)
        stringData = data.decode('UTF-8')
        #
        # Handle commands
        #
    
        #led on
        if stringData.upper() == "LEDON":
            print('Led On')
            ledon()

        #led off
        if stringData.upper() == "LEDOFF":
            print('Led off')
            ledoff()

        #help
        if stringData.upper() == "HELP":
            print('Commands are case insensitive')
            print('ledon - Switch led on')
            print('ledoff - Switch led off')
            print('exit - close server')
            print('help - This help')

        #exit
        if stringData.upper() == "EXIT":
            break 

        conn.sendall(data)
    conn.close()



