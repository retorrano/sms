from serial import Serial
from time import sleep
from datetime import datetime
I_F = open("nums.txt",'r')
M_F = open("message",'r')
contacts = I_F.readlines()
message = M_F.read()
ser = Serial('/dev/ttyUSB0',19200, timeout=2)
cmd = "AT\r"
ser.write(cmd.encode())
sleep(1)
cmd = "AT+CMGF=1\r"
ser.write(cmd.encode())
sleep(1)
i = 0
for c in contacts:
	cmd="AT+CMGS=\"" + c.strip() +"\""
	ser.write(cmd.encode())
	sleep(1)
	cmd="\r"
	ser.write(cmd.encode())
	sleep(1)
	cmd=message.strip() 
	ser.write(cmd.encode())
	sleep(1)
	cmd="\x1A"
	ser.write(cmd.encode())
	sleep(3)
	result = ser.read(400).decode()
	print(result)
	i = i+1
ser.close()
