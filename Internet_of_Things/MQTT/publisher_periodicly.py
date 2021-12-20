import socket
import threading
import mqtt
import time

# Global Variables
IP = socket.gethostbyname(socket.gethostname())
PORT = 1883
BUFFERSIZE = 1024
MSGENCODING = 'utf-8'

def sendTh(MQTTclient):
    while True:
        time.sleep(2)
        MQTTclient.publish('room/light on')
        time.sleep(2)
        MQTTclient.publish('room/light off')


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