#!/usr/bin/env python3

# import the required modules
import time		#helps show timestamps for when the server starts or stops
from http.server import HTTPServer		#python http server library
from server import Server

# define constants to be used when lunching the server
HOST_NAME = 'localhost'
PORT_NUMBER = 8000 #you can use any unoccupied port number

# launching the server block
if __name__ == '__main__':
    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), Server)
    print(time.asctime(), 'Server STARTED - %s:%s' % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), 'Server STOPPED - %s:%s' % (HOST_NAME, PORT_NUMBER))
