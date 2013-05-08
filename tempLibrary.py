#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import config as conf

def tempCurrent():

        sensorFilename = "/sys/bus/w1/devices/" + conf.config['TempSensor']['serial']  + "/w1_slave"
        tfile = open(sensorFilename)
        text=tfile.read()
        tfile.close()
        secondline = text.split("\n") [1]
        temperaturedata = secondline.split(" ") [9]
        temperature = float(temperaturedata[2:])
        temperature=temperature/1000.00

        output = str(temperature);

        return output


