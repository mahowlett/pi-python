#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.append("/home/pi/git/quick2wire-python-api")

import datetime 
from time import sleep
from quick2wire.gpio import pins, Out
from itertools import cycle

def ledon():

	led = pins.pin(5, direction = Out)
	led_state = 1
	with led:
		led.value=1
		sleep(30)
	return "LED on";

ledon()


