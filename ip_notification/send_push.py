import http.client
import urllib
from config import app_token, user_token



def send_push(name):
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
        urllib.parse.urlencode({
            "token": app_token,
            "user": user_token,
            "message": name+ " is online."
        }), {"Content-type": "application/x-www-form-urlencoded"})
    conn.getresponse()
    
def send_startup_push():
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
        urllib.parse.urlencode({
            "token": app_token,
            "user": user_token,
            "message": "IP notifictation has started",
            "title": "IP Checker Started",
            "priority": 0
        }), {"Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()
    print("startup push sent")

