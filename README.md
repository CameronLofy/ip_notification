# ip_notification
Automated python bot to send text or push notification through Pushover when certain IP's are connected to home wifi.


To use, download files and add a file in the same directory as *ip_notification.py* and rename the new file to **config.py** containing your own *ip_list*, *twilio_account*, *twilio_auth*, *twilio_num*, and *user_num* (the number to send the text to)

**Example is shown below:**

### ~~~~ CONFIG.PY ~~~~ ###
```
# Place IP addresses here in this format
ip_list = {"192.168.86.22":"Cameron's Phone",
          "192.168.86.2":"Jon's Phone",
          "192.168.86.3":"Cynthia's Phone"}     # Change IP numbers for your specific use


twilio_account = "ACxxxxxxxxxxxxxxxxxxx"        # Change to your Twilio Account Number
twilio_auth = "0XXXXXXXXXXXXXXXXXXXXX"          # Change to your Twilio Authentication Number

twilio_num = "+14081112222"                     # Change to your number you want to send to
user_num = "+12024445555"                       # Change to your Twilio phone number
```
