import serial
import time


class TextMessage:
	def __init__(self, recipient="+639178558040", message="TextMessage.content not set."):
		self.recipient = recipient
		self.content = message

	def setRecipient(self, number):
		self.recipient = number

	def setContent(self, message):
		self.content = message

	def connectPhone(self):
		self.ser = serial.Serial('/dev/ttyUSB0', 460800, timeout=5, xonxoff = False, rtscts = False, bytesize = serial.EIGHTBITS, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE)
		time.sleep(1)

	def sendMessage(self):
		cmd="AT\r"
		self.ser.write(cmd.encode())
		for i in range(1,100):
			print(self.ser.read(i))
		time.sleep(1)
		self.ser.write(b'AT+CMGF=1\r')
		time.sleep(1)
		self.ser.write(b'''AT+CMGS="''' + self.recipient.encode() + b'''",145\r''')
		self.ser.write(bytes(26))
		time.sleep(1)

	def disconnectPhone(self):
		self.ser.close()
