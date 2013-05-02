#!/usr/bin/python
# -*- coding: utf-8 -*-

from bottle import route, default_app
import subprocess
import sys

@route('/led/test')
def lsTest():
	try:
		output = subprocess.check_output(['python3','--help'])
	except:
		output = 'argh!'
	return output;


@route('/led/on')
def ledOn():
        try:

            output = subprocess.check_output(['python3','/var/www/python/ledOn.py'],stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError, e:
            output =  e.output

        return output;

@route('/led/off')
def ledOff():
        try:
                output = subprocess.check_output(['python3','/var/www/python/ledOff.py'],stderr=subprocess.STDOUT)
        except:
                output = "argh" ;
        return output;


application = default_app()

