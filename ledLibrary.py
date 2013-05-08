#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.append("/home/pi/git/quick2wire-python-api")

import datetime
from time import sleep
from quick2wire.gpio import pins, Out
from itertools import cycle


led = pins.pin(5, direction = Out)
led_state = 1

def ledon():
        led.value=1

def ledoff():
        led.value=0


