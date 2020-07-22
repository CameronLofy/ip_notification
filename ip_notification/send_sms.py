# we import the Twilio client from the dependency we just installed
from twilio.rest import Client
from config import *
# the following line needs your Twilio Account SID and Auth Token
client = Client(twilio_account, twilio_auth)

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
def send_txt(name):
    client.messages.create(to=twilio_num,
                           from_=user_num,
                           body= name + "is online")