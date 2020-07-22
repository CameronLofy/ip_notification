import sys
import subprocess 
from send_sms import send_txt
from config import ip_list


#IP_DEVICE = config('IP_DEVICE')
hostnames = ip_list
notified = {}
for ip in hostnames:
    notified.update({ip:False})


while True:
    for ip in hostnames:
        output = subprocess.Popen(["ping", ip],stdout = subprocess.PIPE).communicate()[0]
        #print(output)
        str_output = str(output, 'utf-8')
        if ("Destination host unreachable" in str_output):
            if notified[ip] == True:
                print(hostnames[ip]," is offline")
            notified[ip] = False
        else:
            if notified[ip] == False:
                send_txt(hostnames[ip])
                print(hostnames[ip]," is online")
            notified[ip] = True
