from serial import Serial
from time import sleep
from datetime import datetime
ser = Serial('/dev/ttyUSB0',19200, timeout=2)
cmd = "AT\r"
ser.write(cmd.encode())
sleep(1)
cmd = "AT+CMGF=1\r"
ser.write(cmd.encode())
sleep(1)
for i in range(1,100):
	cmd="AT+CMGS=\"+639959064795\""
	ser.write(cmd.encode())
	sleep(1)
	cmd="\r"
	ser.write(cmd.encode())
	sleep(1)
	cmd="Hello, i=" + str(i) + ", time: " + str(datetime.now()) 
	ser.write(cmd.encode())
	sleep(1)
	cmd="\x1A"
	ser.write(cmd.encode())
	sleep(3)
	result = ser.read(400).decode()
	print(result)
ser.close()
