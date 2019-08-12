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



Useful links for the packages installation:

    1.  Adafruit_DHT:
            https://github.com/adafruit/Adafruit_Python_DHT

    2.  Influxdb, Grafana and Telegraf:
            https://www.terminalbytes.com/temperature-using-raspberry-pi-grafana/

============================================================================================================
============================================================================================================

Update (2019/8/8):
    Find the bug from influxdb: The influxdb process will use huge memory and lead to the system crash.
    
    Reason: Since there are old configuration files in /etc/telegraf/telegraf.d directory,
    the old measurements in database (dht11) will be merged to new database. The large data samples
    lead to the crash.

    Solution: 
        1.  remove the un-needed configuration files in /eta/telegraf/telegraf.d/

        2.  the default configuration files for the database of influxdb is /etc/influxdb/influxdb.conf.
            We can reset the default configurations like:
            [meta]
            dir = "/home/pi/Data/Influxdb/DHT22_cleanroom_table/influxdb/meta"
            [data]
            dir = "/home/pi/Data/Influxdb/DHT22_cleanroom_table/influxdb/data"
            wal-dir = "/home/pi/Data/Influxdb/DHT22_cleanroom_table/influxdb/wal"
	   
    Please NOTE: If you change the output folder of influxdb database, you should:
                 chown -R influxdb:influxdb  /.... (The new folder)
                 
		 If not, you will get the error: influxb  ...permission deny... blabla


============================================================================================================
============================================================================================================

Update (2019/8/10)
	
	By using the multiple services method, we use different telegraf configration files,
	to using 3 DHT22 sensors.

    Each sensor has specific database in influxdb, so we can vitualize the 3 datas in grafana


============================================================================================================
============================================================================================================


Update (2019/8/11)
	Some bugs were finded, the data of three sensors droped frequently.

	I guess that it was caused by the parallel using of AdafruitDHT programm and leads to the conflict of some
	data.

	So I reduce the data reading frequency with 2 times in one minute. And this bugs happended rarely corresponding.


============================================================================================================
============================================================================================================


Update (2019/8/12)
	Add some descriptions from other people familar with Adafruit_DHT_reader:

    Link:	www.sopwith.ismellsmoke.net/?p=400

    The Adafruit_DHT.read_retry( sensor, pin ) function call will attempt to read data from the sensor 15 times in 2
	second intervals. It returns as soon as is has valid data. This means the function call can take up to 30 seconds
	to return results. After 15 reties it gives up and return None values for the temp and humidity...
	... If you need a temp/humi reading more than once or twice a minute, this device is not for you.





