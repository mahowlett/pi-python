#!/usr/bin/python
# -*- coding: utf-8 -*-

# Echo server program
import socket
import os
import sys
import ledLibrary as ledLib

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen(1)

with ledLib.led:
    while True:
        conn, addr = s.accept()
        print('Connected by', addr)
        data = conn.recv(1024)
        stringData = data.decode('UTF-8')
        #
        # Handle commands
        #
    
        #default behaviour echo sent message back
        response = stringData
        #led on
        if stringData.upper() == "LEDON":
            ledLib.ledon()
            response = 'Led is now on'

        #led off
        if stringData.upper() == "LEDOFF":
            ledLib.ledoff()
            response = 'Led is now off'

        #led status
        if stringData.upper() == "LEDSTATUS":
            answer = ledLib.ledstatus()
            response = 'Led is ' + answer

        #help
        if stringData.upper() == "HELP":
            response = response + 'Commands are case insensitive,'
            response = response + 'ledon - Switch led on,'
            response = response + 'ledoff - Switch led off,'
            response = response + 'exit - close server,'
            response = response + 'help - This help,'

        #exit
        if stringData.upper() == "EXIT":
            break 

        conn.sendall(response.encode('UTF-8'))
    conn.close()


