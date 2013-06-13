#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import config as conf
import logging

sys.path.append(conf.config['Quick2Wire']['libraryLocation'])

from quick2wire.gpio import pins, Out

logging.basicConfig(filename=conf.config['logFile'],level=logging.DEBUG)
led = pins.pin(int(conf.config['Quick2Wire']['led1Pin']), direction = Out)
led_state = 1

def ledon():
    logging.debug('Switch led on')    
    led.value=1

def ledoff():
    logging.debug('Switch led off')
    led.value=0

def ledstatus():
    logging.debug('Led status')
    statusString = 'Off'
    if led.value == 1:
        statusString = 'On'
    return statusString

