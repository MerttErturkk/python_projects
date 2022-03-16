import serial
import serial.tools.list_ports as port_list
import time
import keyboard
    
#DETECT PORT CONNECTIONS AND CHOOSE FIRST AVAILABLE PORT
ports = list(port_list.comports())
print(ports[0].device)

port = ports[0].device
baudrate = 9600
#%% START SERIAL COMMUNICATION
serialPort = serial.Serial(port=port, baudrate=baudrate,
                                bytesize=8, timeout=1, stopbits=serial.STOPBITS_ONE)

print("press '1' for slower blinking\npress '2' for faster blinking")
while True:
    try:  # OTHER KEYS WON'T SHOW ERROR
       if keyboard.is_pressed('1'): 
            serialPort.write(b'1')
            time.sleep(0.1)
       elif keyboard.is_pressed('2'):
            serialPort.write(b'2')
            time.sleep(0.1)
    except:
        time.sleep(0.1)




