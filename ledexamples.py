#!/usr/bin/python
# -*- coding: utf-8 -*-

#export QUICK2WIRE_API_HOME=/home/pi/git/quick2wire-python-api
#export PYTHONPATH=$PYTHONPATH:$QUICK2WIRE_API_HOME
import os


#q2wpath = "/home/pi/git/quick2wire-python-api"
#os.environ['QUICK2WIRE_API_HOME'] = q2wpath
#ppath = os.environ['PYTHONPATH']  
#os.environ['PYTHONPATH']= ppath +':'+q2wpath

import sys
import datetime 
import time
#from quick2wirw.gpio import pins, out

def ledonoff(req):

        #led = pins.pin(24, direction = Out)
	#led_state = 1
	#with led:
	#	led.value=1
#		sleep(0.5)
	#	led.value=0

        output = os.environ;
        return output;


