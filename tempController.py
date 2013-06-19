#!/usr/bin/python
# -*- coding: utf-8 -*-

from bottle import route, default_app
import gpio_client as client

@route('/temp/current')
def currTemp():
        return client.sendCommand('tempcurrent')

@route('/temp/log')
def logTemp():
	return client.sendCommand('templog')

application = default_app()

