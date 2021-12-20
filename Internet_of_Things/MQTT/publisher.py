import socket
import threading
import mqtt

# Global Variables
IP = socket.gethostbyname(socket.gethostname())
PORT = 1883
BUFFERSIZE = 1024
MSGENCODING = 'utf-8'


def sendTh(MQTTclient):
    while True:
        inpt = input("> ").split(' ', 2)

        if (len(inpt) == 3):
            if (inpt[0].upper() == 'PUBLISH'):
                MQTTclient.publish(inpt[1] + ' ' + inpt[2])
        
        elif (len(inpt) == 1 and inpt[0].upper() == 'DISCONNECT'):
            MQTTclient.disconnect()
            MQTTclient.sock.close()
            break

# Entry Point of the Program
def Main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((IP, PORT))

    MQTTclient = mqtt.MQTTclient(sock)

    th = threading.Thread(target=sendTh, args=(MQTTclient,))
    th.start()
    
    MQTTclient.connect('Publisher')

    while True:
        try:
            responseMsg = mqtt.MQTTPackage().parseMsg(sock.recv(BUFFERSIZE))
            print(responseMsg)
        except Exception as e:
            print(e)
            break

    sock.close()

if __name__ == '__main__':
    Main()