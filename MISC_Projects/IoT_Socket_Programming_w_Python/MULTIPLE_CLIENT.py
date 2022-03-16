# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 11:46:58 2021

@author: mertt
"""

import socket
ClientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


print("Waiting for connection")

try:
    ClientSocket.connect((socket.gethostname(), 1234))
except socket.error as e:
    print(str(e))
    
    

Response = ClientSocket.recv(1024)

while True:
    Input = input("your message :")
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    print(Response.decode("utf-8"))