import time
from ipaddress import IPv4Address
from pyairmore.request import AirmoreSession
from pyairmore.services.messaging import MessagingService
I_F_contacts = open("con.csv",'r')
I_F_message = open("message",'r')
I_F_IP = open("ip",'r')
ip = I_F_IP.read().strip()
print(ip)
F_F=open("Failed.csv",'w')
raw_message = I_F_message.read().strip()
contacts = I_F_contacts.readlines()
session = AirmoreSession(ip)
service = MessagingService(session)
was_accepted = session.request_authorization()
print(was_accepted)
for c in contacts:
    try:        
        message = raw_message
        print("Sending message " + message + "to " + c)
        service.send_message(c,message)
        time.sleep(2)
    except Exception as e:
        F_F.write(c)
        print(e)
F_F.close()
I_F_contacts.close()
I_F_message.close()
I_F_IP.close()

