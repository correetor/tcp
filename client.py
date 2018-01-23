#!/usr/bin/env python

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5021
BUFFER_SIZE = 1024
MESSAGE = raw_input("Number for fac : ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
print("received data:"+data)
raw_input("Number for fac : ")

s.close()
