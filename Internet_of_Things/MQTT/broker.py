import socket
import threading
import traceback
import mqtt

# Global Variables
IP = socket.gethostbyname(socket.gethostname())
PORT = 1883
BUFFERSIZE = 1024
MSGENCODING = 'utf-8'
topics = {}

def mqttHandleMsg(msg, conn, addr):
    parsedMsg = mqtt.MQTTPackage().parseMsg(msg)
    payload = parsedMsg.payload 
    
    print(addr, ": ", parsedMsg)

    if (parsedMsg.msgType == 3):    # PUBLISH
        if (len(payload.split(' ', 1)) < 2):
            print("Not enough arguments!")
            return

        # Seperating payload to topic and value
        topicStr, value = payload.split(' ', 1)

        if (topicStr in topics): # If topic exists
            topic = topics[topicStr]
            topic.lastMsg = value
            # Sending content to the subscribers of the topic 
            for sub in topic.subscribers:
                sub[0].send(mqtt.MQTTPackage(3, 0, 0, 0).wrapMsg(payload.encode(MSGENCODING)))
        else: # If topic doesn't exist
            # Creating new topic
            newTopic = mqtt.Topic()
            newTopic.lastMsg = value
            topics[topicStr] = newTopic

        conn.send(mqtt.MQTTPackage(4, 0, 0, 0).wrapMsg(payload.encode(MSGENCODING)))
    
    elif (parsedMsg.msgType == 8):  # SUBSCRIBE

        if (payload in topics): # If the topic exists
            topic = topics[payload]

            if ((conn, addr) not in topic.subscribers): # If sub didnt already sub to the topic
                # Adding subscriber to the topic
                topic.addSub((conn, addr))

                if (topic.lastMsg != None): # Sending retained message
                    conn.send(mqtt.MQTTPackage(9, 0, 0, 1).wrapMsg(f"{payload} {topic.lastMsg}".encode(MSGENCODING)))

            else:
                print("Already in the topic!")
                pass 
        else:
            print(f"Topic<{payload}> does not exist!")
            pass # Topic does not exist

    elif (parsedMsg.msgType == 10): # UNSUBSCRIBE
        if (payload in topics): # If the topic exists
            topic = topics[payload]

            if ((conn, addr) in topic.subscribers): # If sub didnt already sub to the topic
                # Adding subscriber to the topic
                topic.removeSub((conn, addr))
                conn.send(mqtt.MQTTPackage(11, 0, 0, 0).wrapMsg(payload.encode(MSGENCODING)))
            else:
                print("Subscriber is not inside the topic!")
        else:
            print(f"Topic<{payload}> does not exist!")
    
    elif (parsedMsg.msgType == 1):  # CONNECT
        conn.send(mqtt.MQTTPackage(2, 0, 0, 0).wrapMsg(payload.encode(MSGENCODING)))



# Function for thread which handle client messages
def handleClientTh(conn, addr):
    while True:
        try:
            msg = conn.recv(BUFFERSIZE)

            if not msg:
                break
            else:
                mqttHandleMsg(msg, conn, addr)

        except ConnectionResetError as e:
            print(f'{addr} DISCONNECTED!')
            for _,topic in topics.items():
                if ((conn, addr) in topic.subscribers):
                    topic.removeSub((conn, addr))
            break

    conn.close()

# Entry Point of Program
def Main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    sock.bind((IP, PORT))
    sock.listen(5)

    print('BROKER IS RUNNING!')

    while True:
        try:
            conn, addr = sock.accept()
            th = threading.Thread(target=handleClientTh, args=(conn, addr))
            th.start()
            print(f'{addr} CONNECTED!')
        except:
            traceback.print_exc()
            break

    sock.close()

if __name__ == '__main__':
    Main()