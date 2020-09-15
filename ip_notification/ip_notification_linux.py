import sys
import subprocess
import pingparsing
import datetime
import time
#from send_sms import *
from send_push import *
from config import ip_list


#IP_DEVICE = config('IP_DEVICE')
hostnames = ip_list
notified = {}
ip_times = {}
current_time = datetime.datetime.now()
print(current_time)

for ip in hostnames:
    notified.update({ip:False})
    ip_times.update({ip:{'offline':current_time, 'online':current_time}})
print(ip_times)

send_startup_push()


# Forever looping to check which IPs are connected to wifi
while True:
    
    # Looing through list of IPs to check
    # TODO: Speed up ping commmand search time
    for ip in hostnames:
        
        #output = subprocess.Popen(["ping", "-c", "1", ip],stdout = subprocess.PIPE).communicate()[0]
        #str_output = str(output, 'utf-8')
        
        output = pingparsing.PingParsing()
        transmitter = pingparsing.PingTransmitter()
        transmitter.destination = ip
        transmitter.count = 1
        result = str(transmitter.ping())
        #print(result)
        

        # If IP is offline, the output will have "Destination host unreachable"
        if ("0 received" in result) or ("Destination Host Unreachable" in result):
            if notified[ip] == True:
                print(hostnames[ip],' is offline')
                ip_times[ip]['offline'] = datetime.datetime.now()
                
            notified[ip] = False

        #elif("Reply from {ip}" in str_output):
        else:
            if notified[ip] == False:
                # Using the send_sms function in send_sms.py
                ip_times[ip]['online'] = datetime.datetime.now()
                #print(f"Last time logged online for {hostnames[ip]}: {ip_times[ip]['online']}")
                #print(f"Last time logged offline for {hostnames[ip]}: {ip_times[ip]['offline']}")
                time_delta = (ip_times[ip]['online']-ip_times[ip]['offline'])
                #print(f"Time since offline for {hostnames[ip]}: {time_delta}")
                time_diff = time_delta.total_seconds()/60
                #print(hostnames[ip],' is online')
                if(time_diff >= 60 and datetime.datetime.now().hour >= 9):
                    send_push(hostnames[ip])
                    print("notification sent!")
                
            notified[ip] = True
