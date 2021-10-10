import time
import serial


def send_sms(num, mes):
	phone = serial.Serial("/dev/ttyUSB0", 460800, timeout=5)
	print(phone.name)
	print(phone.read(100))
	try:
		time.sleep(0.5)
		time.sleep(0.5)
		phone.write(b'ATZ\r')
		time.sleep(0.5)
		phone.write(b'AT+CMGF=1\r')
		time.sleep(0.5)
		phone.write(b'AT+CMGS="' + num.encode() + b'"\r')
		time.sleep(0.5)
		phone.write(mes.encode() + b"\r")
		time.sleep(0.5)
		phone.write(bytes([26]))
		time.sleep(0.5)
		print(phone.readall())
	except:
		print("x")	
	finally:
		phone.close


	
