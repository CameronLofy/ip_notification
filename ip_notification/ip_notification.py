import sys
import subprocess 
import datetime
from send_sms import send_txt
from config import ip_list


#IP_DEVICE = config('IP_DEVICE')
hostnames = ip_list
notified = {}
for ip in hostnames:
    notified.update({ip:False})
    ip_times.update({ip:{'offline':current_time, 'online':current_time}})


# Forever looping to check which IPs are connected to wifi
while True:

    # Looing through list of IPs to check
    # TODO: Speed up ping commmand search time
    for ip in hostnames:
        output = subprocess.Popen(["ping", "-n", "1", ip],stdout = subprocess.PIPE).communicate()[0]
        str_output = str(output, 'utf-8')

        # If IP is offline, the output will have "Destination host unreachable"
        if ("timed out" in str_output) or ("Destination host unreachable" in str_output):
            if notified[ip] == True:
                print(hostnames[ip]," is offline")
                ip_times[ip]['offline'] = datetime.datetime.now()
            notified[ip] = False

        #elif("Reply from {ip}" in str_output):
        else:
            if notified[ip] == False:
                # Using the send_sms function in send_sms.py
                ip_times[ip]['online'] = datetime.datetime.now()
                print(f"Last time logged online for  {hostnames[ip]}: {ip_times[ip]['online']}")
                print(f"Last time logged offline for {hostnames[ip]}: {ip_times[ip]['offline']}")
                time_delta = (ip_times[ip]['online']-ip_times[ip]['offline'])
                print(f"Time since offline for {hostnames[ip]}: {time_delta}")
                time_diff = time_delta.total_seconds()/60
                print(hostnames[ip],' is online')
                if(time_diff >= 10):
                    send_txt(hostnames[ip])
                    print("text sent!")
            notified[ip] = True

