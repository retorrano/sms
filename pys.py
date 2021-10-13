from serial import Serial
from time import sleep
from datetime import datetime
ser = Serial('/dev/ttyUSB4',19200, timeout=0)
cmd = "AT\r"
ser.write(cmd.encode())
print(ser.read(400))
sleep(3)
cmd = "AT+CSCA=\"+639170000130\",145\r"
ser.write(cmd.encode())
print(ser.read(400))
sleep(3)
cmd = "AT+CMGF=1\r"
ser.write(cmd.encode())
sleep(3)
print(ser.read(400))
succ="N"
t=1
while succ == "N":
	print("try :" + str(t) + " times")
	cmd = "AT+CSCS=\"GSM\"\r"
	ser.write(cmd.encode())
	print(ser.read(400))
	cmd = "AT+CSCS?\r"
	ser.write(cmd.encode())
	sleep(3)
	print(ser.read(400))
	cmd = "AT+CMGS=\"+639959064795\",145\rTest Quake\x1A"
	ser.write(cmd.encode())
	sleep(3)
	result = ser.read(400)
	print(result)
	cmd = "AT+CSCS?\r"
	ser.write(cmd.encode())
	sleep(3)
	print(ser.read(400))
	if "OK" not in str(result):
		succ = "N"
	else:
		succ = "Y" 
	t = t+1
	ser.flush()
ser.close()
