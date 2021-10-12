import sms2
sms = sms2.TextMessage("+639959064795","BAL")
sms.connectPhone()
sms.sendMessage()
sms.disconnectPhone()
print("message sent successfully")
