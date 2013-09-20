#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import config as conf
import mysql.connector
import datetime
import time
import logging

con = None

logging.basicConfig(filename=conf.config['logFile'],level=logging.DEBUG)

def num (s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def tempCurrent():
        logging.debug('Current temperature reading')
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
        con = None
        try:
            con = mysql.connector.connect(user='root', password=conf.config['localDb']['Password'], host='localhost', database='test')
            cur = con.cursor()

            temperature=tempCurrent()
            logging.debug('Logged temp is: %f ',num(temperature))    
            currdatetime = datetime.datetime.now().isoformat()
            statement  = "INSERT INTO temps(temp,time) VALUES(%f,'%s')" % (num(temperature),currdatetime)
            cur.execute(statement)
            con.commit()
            output = "Logged OK"
        except mysql.connector.Error as err:
                output = "Logging failed"
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Something is wrong with your user name or password")
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not exists")
                else:
                    print(err)
        finally:
                if con:
                        con.close()
        return output
