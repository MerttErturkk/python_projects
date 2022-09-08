import socket
# Socket is the end point that recieves the data

# create socket object
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#since we use one machine we connect to the hostname
s.connect((socket.gethostname(),1234))



full_msg= ""
while True:
    msg=s.recv(8) # BUFFER SIZE (1024 is more than enough)
    
    if len(msg) <=0:
        break
    full_msg += msg.decode("utf-8")
    print(msg.decode("utf-8"))

