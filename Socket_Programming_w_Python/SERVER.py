import socket
import time
# Socket is the end point that recieves the data
HEADERSIZE=10


# create socket object
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# family type is af_inet, (IPv4)
# socket type is sock_stream (TCP) streaming

# end point sits at an IP and a port
s.bind((socket.gethostname(), 1234))

s.listen(5) # with a queue of 5 

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established !")
    
    
    msg = "Welcome to the server!"
    data = f"{len(msg):<{HEADERSIZE}}" + msg
    # "<" stands for left alignment

    clientsocket.send(bytes(data,"utf-8"))
    
    while True:
        time.sleep(3)
        msg= f"The time is {time.time()}"
        data=f"{len(msg):<{HEADERSIZE}}"+msg
        clientsocket.send(bytes(data,"utf-8"))
    #clientsocket.close()
    