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
		self.ser.write(b'ATZ\r')
		time.sleep(1)
		self.ser.write(b'AT+CMGF=1\r')
		time.sleep(1)
		self.ser.write(b'''AT+CMGS="''' + self.recipient.encode() + b'''"\r''')
		time.sleep(1)
		self.ser.write(self.content.encode() + b"\r")
		time.sleep(1)
		self.ser.write(bytes(26))
		time.sleep(1)

	def disconnectPhone(self):
		self.ser.close()
