import serial
import serial.tools.list_ports as port_list
import time
    
#DETECT PORT CONNECTIONS AND CHOOSE FIRST AVAILABLE PORT
ports = list(port_list.comports())
print(ports[0].device)

port = ports[0].device
baudrate = 9600
#%% START SERIAL COMMUNICATION
serialPort = serial.Serial(port=port, baudrate=baudrate,
                                bytesize=8, timeout=1, stopbits=serial.STOPBITS_ONE)

while True:
    line = int.from_bytes(serialPort.read(),"little")
    print(line)
    time.sleep(1)

#serialPort.write(b'1')





