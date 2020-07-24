import sys
import subprocess 
from send_sms import send_txt
from config import ip_list


#IP_DEVICE = config('IP_DEVICE')
hostnames = ip_list
notified = {}
for ip in hostnames:
    notified.update({ip:False})


# Forever looping to check which IPs are connected to wifi
while True:

    # Looing through list of IPs to check
    # TODO: Speed up ping commmand search time
    for ip in hostnames:
        output = subprocess.Popen(["ping", "-n", "1", ip],stdout = subprocess.PIPE).communicate()[0]
        str_output = str(output, 'utf-8')

        # If IP is offline, the output will have "Destinatino host unreachable"
        if ("timed out" in str_output) or ("Destination host unreachable" in str_output):
            if notified[ip] == True:
                print(hostnames[ip]," is offline")
            notified[ip] = False

        #elif("Reply from {ip}" in str_output):
        else:
            if notified[ip] == False:
                # Using the send_sms function in send_sms.py
                send_txt(hostnames[ip])
                print(hostnames[ip]," is online")
            notified[ip] = True

