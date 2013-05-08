#!/usr/bin/python
# -*- coding: utf-8 -*-

from bottle import route, default_app
import subprocess, socket
import sys

HOST = socket.gethostbyname(socket.gethostname())
PORT = 50007            # The same port as used by the server

@route('/led/test')
def lsTest():
	try:
		output = subprocess.check_output(['python3','--help'])
	except:
		output = 'argh!'
	return output;

@route('/led/on')
def ledOn():
        return ledControl('ledon')

@route('/led/off')
def ledOff():
        return ledControl('ledoff')

@route('/led/status')
def ledStatus():
	return ledControl('ledstatus')

def ledControl(command):
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

