import sms2
sms = sms2.TextMessage("222","BAL")
sms.connectPhone()
sms.sendMessage()
sms.disconnectPhone()
print("message sent successfully")
