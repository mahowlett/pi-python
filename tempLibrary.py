#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

def tempCurrent():

        tfile = open("/sys/bus/w1/devices/28-000003c238ec/w1_slave")
        text=tfile.read()
        tfile.close()
        secondline = text.split("\n") [1]
        temperaturedata = secondline.split(" ") [9]
        temperature = float(temperaturedata[2:])
        temperature=temperature/1000.00

        output = str(temperature);

        return output


