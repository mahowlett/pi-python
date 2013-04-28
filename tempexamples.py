#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import datetime 
import time
import config


con = None

def currtemp(req):

        req.content_type = 'text/html'

        tfile = open("/sys/bus/w1/devices/28-000003c238ec/w1_slave")
	text=tfile.read()
	tfile.close()
	secondline = text.split("\n") [1]
	temperaturedata = secondline.split(" ") [9]
	temperature = float(temperaturedata[2:])
	temperature=temperature/1000.00

        output = "Temperature is %.2f " % temperature;
        return output;

def mysqltemplogger(req):
	output=""
	req.content_type = 'text/html'
	try:
		con = mdb.connect('localhost','root',config.dbPassword,'test')
		cur = con.cursor()
		tfile = open("/sys/bus/w1/devices/28-000003c238ec/w1_slave")
		text=tfile.read()
		tfile.close()
		secondline = text.split("\n")[1]
		temperaturedata = secondline.split(" ") [9]
		temperature = float(temperaturedata[2:])
		temperature=temperature/1000.00
		currdatetime = datetime.datetime.now().isoformat()
		statement  = "INSERT INTO temps(temp,time) VALUES(%f,'%s')" % (temperature,currdatetime)
		cur.execute(statement)
		con.commit()
		output = output + "\n Temperature Logged was %f" % temperature;
	except mdb.Error, e:
		output = "Error %d %s" % (e.args[0], e.args[1]);
	finally:
		if con:
			con.close()
	return output

