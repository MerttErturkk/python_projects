import socket
import pickle
HEADERSIZE=10

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))
while True:
    full_msg= b""
    new_msg= True
    while True:
        msg=s.recv(16) 
        if new_msg:
            try:
                msglen=int(msg[:HEADERSIZE])
                print(f"new message length: {msg[:HEADERSIZE]}")
            except ValueError:
                pass
            new_msg= False
            
        full_msg += msg
        
        if len(full_msg)-HEADERSIZE == msglen:
            print("full message recieved")
            print(full_msg)
            
            
            d=pickle.loads(full_msg[HEADERSIZE:])
            print(d)
            new_msg = True
            full_msg =b""
    print(full_msg)