#!/usr/bin/python
# -*- coding: utf-8 -*-

from bottle import route, default_app
import subprocess, socket
import sys

HOST = socket.gethostbyname(socket.gethostname())
PORT = 50007            # The same port as used by the server

@route('/temp/current')
def currTemp():
        return tempControl('tempcurrent')

def tempControl(command):
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

application = default_app()

