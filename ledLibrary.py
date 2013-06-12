#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import config as conf
import logging

sys.path.append(conf.config['Quick2Wire']['libraryLocation'])

import datetime
from quick2wire.gpio import pins, Out
from itertools import cycle

logging.basicConfig(filename=conf.config['logFile'],level=logging.DEBUG)
led = pins.pin(int(conf.config['Quick2Wire']['led1Pin']), direction = Out)
led_state = 1

def ledon():
    logging.debug('Switch led on')    
    led.value=1

def ledoff():
    led.value=0

def ledstatus():
    statusString = 'Off'
    if led.value == 1:
        statusString = 'On'
    return statusString

