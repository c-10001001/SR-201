#!/bin/python
#
# Author: 001100010010011110100001101101110011
#
# Function: Netcat implementation to obtain SR-201 relay status.
#
# Source http://stackoverflow.com/questions/1908878/netcat-implementation-in-python#1909355

import socket
import sys

RED='\033[31m' # Sets color but is unused a.t.m.

host = sys.argv[1] # IP of the relay to control
port = sys.argv[2] # The port to use 6722 for TCP, 6723 for UDP
command = sys.argv[3] # The command to execute. 

'''
Valid commands:
00 Obtain relay status, toggles nothing.
11 Turn relay 1 on
21 Turn relay 1 off
12 Turn relay 2 on
22 Turn relay 2 off

Status output and command return values.
00000000 All relays off
01000000 2nd relay on
10000000 1st relay on
11000000 All relays on
'''

val_cmds = ['00','11','12','21','22']
  

# check variables.
def val_vars(host, port, command):
    valid = False
    parts = host.split(".")
    # If host was not split into 4 octets False will be returned for Valid..
    if len(parts) != 4:
        print "Invalid IPv4"
        return valid
    
    # Check if octects lie between 1 and 255.
    for item in parts:
        if item.isdigit():
            if not 0 <= int(item) <= 255:
                print "False not <255"
                return valid
        else:  
            print item, "leverde een fout op."
            return valid    
    
    # Check if supplied command is valid.
    if command not in val_cmds:
        return valid
        print "Ongeldig commando:", command, """
        Geldige invoer is: 
        11 \trelay 1 on
        12 \trelay 2 on
        21 \trelay 1 off
        22 \trelay 2 off
        """
    
    # Check if supplied port is valid.
    if port.isdigit(): 
        if not 1000 >= int(port) <= 65000:
            # print "Port:", port
            valid = True
        else:
            valid = False
            print "Invalid port number:", port

    return valid


def netcat(host, port, command):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.sendall(command)
        s.shutdown(socket.SHUT_WR)
        while 1:
	    data = s.recv(1024)
	    if data == "":
		    break
	    print "Received:", repr(data)
        # print "Connection closed."
        s.close()


# Only start script when 3 arguments have been supplied and valid is True.
if len(sys.argv) == 4:
    #print "Debug handle" # used to verify is execution routine is hit. 
    valid = val_vars(host, port, command)
    if valid == True:
        netcat(host, int(port), command)   
    else:
	print "One or more argument checks failed, verify the input."
else:
    print "input error, incorrect ammount of arguments."
    quit()


