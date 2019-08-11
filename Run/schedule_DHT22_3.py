#!/usr/bin/python
# Run the DHT22 sensor temperature and humidity reading 30 time per minute

import os, time

cmd = 'python /home/pi/Work/DHT22/Run/run_DHT22_3.py'
#cmd = 'python /home/pi/Work/DHT22/Run/dht22.py'
for t in range(1, 60, 31):
    #print(t)
    os.system(cmd)
    time.sleep(30)
