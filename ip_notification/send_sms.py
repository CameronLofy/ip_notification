from twilio.rest import Client
from config import *

# the following line needs your Twilio Account SID and Auth Token
client = Client(twilio_account, twilio_auth)

# to fill the twilio_account, twilio_auth, twilio_num, and user_num
# create a file called config.py with the values of these variables
# as shown below in this config.py format:

""" 
# config.py
# Place IP addresses here in this format
ip_list = {"192.168.86.22":"Cameron's Phone",
		   "192.168.86.2":"Jon's Phone",
		   "192.168.86.3":"Cynthia's Phone"}


twilio_account = "ACxxxxxxxxxxxxxxxxx"
twilio_auth = "xxxxxxxxxxxxxxxxxxxxx"

twilio_num = "+1XXXXXXXXXX"
user_num = "+1XXXXXXXXXX"

"""




def send_txt(name):
    client.messages.create(to=twilio_num,
                           from_=user_num,
                           body= name + "is online")



#