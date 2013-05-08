#!/usr/bin/python
# -*- coding: utf-8 -*-

from bottle import route, default_app
import gpio_client as client

@route('/temp/current')
def currTemp():
        return client.sendCommand('tempcurrent')

application = default_app()

