#!/usr/bin/python
# -*- coding: utf-8 -*-

from bottle import route, default_app
import gpio_client as client
import config as conf
import logging

logging.basicConfig(filename=conf.config['logFile'],level=logging.DEBUG)
@route('/temp/current')
def currTemp():
        logging.debug('temp controller tempcurrent')
        return client.sendCommand('tempcurrent')

@route('/temp/log')
def logTemp():
	logging.debug('temp controller templog')
        return client.sendCommand('templog')

application = default_app()

