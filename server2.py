#!/usr/bin/env python

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5006
BUFFER_SIZE = 409600000  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    myfile = open("result.png", 'wb')
    myfile.write(data)
    myfile.close()
conn.close()
