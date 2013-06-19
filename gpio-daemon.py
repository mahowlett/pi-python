#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys, time
import socket
import os
import config as conf
import logging
import ledLibrary as ledLib
import tempLibrary as tempLib
from subprocess import call

from daemon import daemon

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = int(conf.config['RPCServer']['Port'])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

logging.basicConfig(filename=conf.config['logFile'],level=logging.DEBUG)

class MyDaemon(daemon):
        def run(self):
            with ledLib.led:
                s.bind((HOST, PORT))
                s.listen(1)
                logging.debug('GPIO daemon run called')
                while True:
                    try:
                        conn, addr = s.accept()

                        data = conn.recv(1024)
                        stringData = data.decode(conf.config['encoding'])
                        #
                        # Handle commands
                        #

                        logging.debug('GPIO Daemon command - %s' % (stringData.upper()))
                        #default behaviour echo sent message back
                        response = stringData

                        #led on
                        if stringData.upper() == "LEDON":
                            ledLib.ledon()
                            response = 'Led is now on'

                        #led off
                        if stringData.upper() == "LEDOFF":
                            ledLib.ledoff()
                            response = 'Led is now off'

                        #led status
                        if stringData.upper() == "LEDSTATUS":
                            answer = ledLib.ledstatus()
                            response = 'Led is ' + answer

                        #temp (current)
                        if stringData.upper() == "TEMPCURRENT":
                            answer = tempLib.tempCurrent()
                            response = 'Temperature is ' + answer + ' degrees centigrade'

                        #log temperature
                        if stringData.upper() == "TEMPLOG":
                            if tempLib.tempLog():
                                response = 'Temperature Logged'
                            else:
                                response = 'Could not log the temperature'

                        #help
                        if stringData.upper() == "HELP":
                            response = response + 'Commands are case insensitive,'
                            response = response + 'ledon - Switch led on,'
                            response = response + 'ledoff - Switch led off,'
                            response = response + 'exit - close server,'
                            response = response + 'help - This help,'

                        conn.sendall(response.encode(conf.config['encoding']))
                    except socket.error as  e:
                        logging.debug("socket error %d (%s)" % (e.errno, e.strerror))
                    #finally:
                        logging.debug('closing sockets')
                        conn.close()
        def stop(self):
            super(MyDaemon,self).stop()
        def start(self):
            logging.debug('Overridden start()')
            call(["gpio-admin","unexport","24"])
            super(MyDaemon,self).start()

if __name__ == "__main__":
        daemon = MyDaemon('/tmp/daemon-example.pid')
        if len(sys.argv) == 2:
                if 'start' == sys.argv[1]:
                        daemon.start()
                elif 'stop' == sys.argv[1]:
                        daemon.stop()
                elif 'restart' == sys.argv[1]:
                        daemon.restart()
                #for debugging purposes run in foreground
                elif 'run' == sys.argv[1]:
                        daemon.run()
                else:
                        print("Unknown command")
                        sys.exit(2)
                sys.exit(0)
        else:
                print("usage: %s start|stop|restart|run" % sys.argv[0])
                sys.exit(2)

