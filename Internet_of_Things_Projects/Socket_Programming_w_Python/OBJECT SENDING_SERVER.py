import socket
import pickle
HEADERSIZE=10


s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5) # with a queue of 5 



while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established !")
    
    d={"a":"HEY",
       "b":"THERE"}
    msg=pickle.dumps(d)
    
    msg = bytes(f"{len(msg):<{HEADERSIZE}}","utf-8") + msg
    clientsocket.send(msg)
    
    clientsocket.close()
    