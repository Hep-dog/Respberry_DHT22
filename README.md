### This project is used to read the temperature and humidity values using the DHT11/DHT22 sensor for Raspberry
### The core package is the Adafruit_DHT
### Author: Jiyizi 
### Any problem you can contact: shenpx@ihep.ac.cn

The softwares needed:

1.  Influxdb  ( database )
2.  Telegraf  ( input the local results obtained from sensor readout to Influxdb )
3.  Grafana   ( Visualization of the data in database )


A:  You should run the influxdb and grafana auto after the Raspberry starting-up:
    sudo systemctl enable influxdb
    sudo systemctl enable grafana
    sudo systemctl enable telegraf

    The script to collect data using DHT11/22 sensor is: 
    ./Run/run.py   (collect single data once)

B:  To collect the data collection, we use the crontab command:
    sudo crontab -e  (sudo is needed here)
    the script is ./Run/schedule.py

C:  Notes for the configurations for softwares:

    You should create the database in Influxdb:
    1. influx
    2. create database DHT22

    You should add the configuration file for the telegraf to configuring the data format to database:
    telegraf  --config  temperatureLog.conf  (You should give you local IP and you database name for influxdb)

