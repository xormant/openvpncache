import os
import datetime
import time
import requests
import json

while True:
    getips = os.popen(''' cat /var/log/syslog | grep -n "Incoming Data Channel" | grep -E -o "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)" ''').read().strip("\n").strip("'").strip(']').strip('[')
    getipslist = os.popen(''' cat /var/log/syslog | grep -n "Incoming Data Channel" | grep -E -o "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)" | wc -l ''').read().strip("\n").strip("'").strip(']').strip('[')
    getipslist2 = int(getipslist)
    if getipslist2 >= 1:
        dupcheck = os.system(f"ipset test caching {getips}")
        if dupcheck == 0:
            print("already added")
            os.system("truncate -s 0 /var/log/syslog")
        else:
            print(f"added {getips} to cache")
            os.system(f"ipset add caching {getips}")
            os.system(f"echo '{getips}' >> /root/tmp/cachedips.txt")
        os.system("truncate -s 0 /var/log/syslog")
    else:
        print("snooping")
        time.sleep(1)