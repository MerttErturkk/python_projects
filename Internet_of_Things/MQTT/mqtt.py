class Topic:
    def __init__(self):
        self.subscribers = [] # Subscriber List
        self.lastMsg = None  # Retain the last message  
    
    def addSub(self, conn): # append new subscriber to list
        self.subscribers.append(conn)

    def removeSub(self, conn): # remove sub when it unsubs
        self.subscribers.remove(conn)

class MQTTclient:
    def __init__(self, socket):
        self.sock = socket
    
    def connect(self, payload, DUP = 0, QoS = 0, retain = 0):
        self.sock.send(MQTTPackage(1, DUP, QoS, retain).wrapMsg(payload.encode('utf-8')))

    def subscribe(self, topic, DUP = 0, QoS = 0, retain = 0):
        self.sock.send(MQTTPackage(8, DUP, QoS, retain).wrapMsg(topic.encode('utf-8')))
    
    def unsubscribe(self, topic, DUP = 0, QoS = 0, retain = 0):
        self.sock.send(MQTTPackage(10, DUP, QoS, retain).wrapMsg(topic.encode('utf-8')))

    def publish(self, msg, DUP = 0, QoS = 0, retain = 0):
        self.sock.send(MQTTPackage(3, DUP, QoS, retain).wrapMsg(msg.encode('utf-8')))
    
    def disconnect(self, DUP = 0, QoS = 0, retain = 0):
        self.sock.send(MQTTPackage(14, DUP, QoS, retain).wrapMsg())

class MQTTPackage:
    def __init__(self, msgType = 0, DUP = 0, QoS = 0, retain = 0):
        self.msgType = msgType
        self.DUP = DUP
        self.QoS = QoS
        self.retain = retain
        self.remainingLength = None
        self.payload = None

    def wrapMsg(self, msg = b''): # takes string as byte 
        header = bytearray(2) # create two byte long header

        header[0] = self.msgType << 4
        header[0] |= self.DUP << 3
        header[0] |= self.QoS << 1
        header[0] |= self.retain
        header[1] = len(msg) # add the length of the message 

        wrappedMsg = header + msg 
        return wrappedMsg
    
    def __str__(self):
        return f"[{msgTypeName(self.msgType)}, {self.DUP}, {self.QoS}, {self.retain} | {self.remainingLength}] [{self.payload}]"

    def parseMsg(self, msg):
        header = bytearray(1)
        header[0] = msg[0]
        
        self.msgType = header[0] >> 4
        self.DUP = (header[0] & 0b00001000) >> 3
        self.QoS = (header[0] & 0b00000110) >> 1
        self.retain = header[0] & 0b00000001
        self.remainingLength = msg[1]
        self.payload = msg[2:].decode('utf-8')

        return self

def msgTypeName(msgType):
    if (msgType == 0):
        return 'Reserved'
    elif (msgType == 1):
        return 'CONNECT'
    elif (msgType == 2):
        return 'CONNACK'
    elif (msgType == 3):
        return 'PUBLISH'
    elif (msgType == 4):
        return 'PUBACK'
    elif (msgType == 5):
        return 'PUBREC'
    elif (msgType == 6):
        return 'PUBREL'
    elif (msgType == 7):
        return 'PUBCOMP'
    elif (msgType == 8):
        return 'SUBSCRIBE'
    elif (msgType == 9):
        return 'SUBACK'
    elif (msgType == 10):
        return 'UNSUBSCRIBE'
    elif (msgType == 11):
        return 'UNSUBACK'
    elif (msgType == 12):
        return 'PINGREQ'
    elif (msgType == 13):
        return 'PINGRESP'
    elif (msgType == 14):
        return 'DISCONNECT'
    elif (msgType == 15):
        return 'Reserved'
    else:
        return 'Undefined'