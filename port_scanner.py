#!/usr/bin/env python

# learned from http://www.pythonforbeginners.com/code-snippets-source-code/port-scanner-in-python

import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('clear', shell=True)

remoteServer    = raw_input("Enter a remote host to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)

print "Now scanning "+remoteServerIP
t1 = datetime.now()

try:
    for port in range(1,1025):
        print "\tScanning port " + str(port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        result = sock.connect_ex((remoteServerIP, port))
        ttemp = datetime.now()
        tsocket = ttemp-t1
        print "That took ", tsocket
        if result == 0:
            print "\t\tPort {}:\tOpen".format(port)
        sock.close()

except KeyboardInterrupt:
    print "Now exiting..."
    sys.exit()

except socket.gaierror:
    print "Hostname could not be resolved. Now exiting..."
    sys.exit()

except socket.error:
    print "Couldn't connect to server"
    sys.exit()

t2 = datetime.now()

total = t2 - t1

print "Scan completed in ", total
