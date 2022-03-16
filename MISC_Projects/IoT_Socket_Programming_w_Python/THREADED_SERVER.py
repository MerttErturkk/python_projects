# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 11:30:05 2021

@author: mertt
"""

import socket
from _thread import start_new_thread
HEADERSIZE=10
ThreadCount = 0
ServerSocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    ServerSocket.bind((socket.gethostname(), 1234))
except socket.error as e:
    print(str(e))
    
print("Waiting for a connection..")
ServerSocket.listen(5)


def threaded_client(connection):
    connection.send(str.encode("Welcome to the server"))
    
    while True:
        data = connection.recv(2048)
        reply= "Server says " +data.decode("utf-8")
        if not data:
            break
        connection.sendall(str.encode(reply))
    
    connection.close()


while True:
    Client,address = ServerSocket.accept()
    print("Connected to: " + address[0]+ ":" +str(address[1]))
    start_new_thread(threaded_client,(Client, ))
    
    ThreadCount +=1
    
    print("Thread Number: " +str(ThreadCount))
    
ServerSocket.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    