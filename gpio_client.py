#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import sys
import config as conf

HOST = socket.gethostbyname(socket.gethostname())
PORT = int(conf.config['RPCServer']['Port'])

def sendCommand(command):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))
            s.sendall(bytes(command))
            data = s.recv(1024)
            s.close()
            output = 'Received: ' + data
        except OSError as msg:
            output =  msg
        finally:
            s.close()
        return output;

