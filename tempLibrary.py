#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import config as conf
#import pymysql as mdb
import datetime
import time

con = None

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

def tempLog():
        output="" 
        try:
            #con = mdb.connect('localhost','root',config.dbPassword,'test')
            #cur = con.cursor()

            temperature=tempCurrent()
                
            currdatetime = datetime.datetime.now().isoformat()
            statement  = "INSERT INTO temps(temp,time) VALUES(%f,'%s')" % (temperature,currdatetime)
            #cur.execute(statement)
            #con.commit()
            output = True
        except mdb.Error as e:
                output = False
        finally:
                if con:
                        con.close()
        return output
