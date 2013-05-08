#!/usr/bin/python
# -*- coding: utf-8 -*-

from bottle import route, default_app
import gpio_client as client

@route('/led/on')
def ledOn():
        return client.sendCommand('ledon')

@route('/led/off')
def ledOff():
        return client.sendCommand('ledoff')

@route('/led/status')
def ledStatus():
	return client.sendCommand('ledstatus')

application = default_app()

