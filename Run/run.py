import Adafruit_DHT as dht
import logging
import time


logging.basicConfig( filename='/home/pi/Work/DHT22/Run/Log/Temp_Humi.log', filemode='a', format='%(created)f %(message)s', level=logging.INFO)


def run_collection():
    while True:
        #h, t= dht.read_retry( dht.DHT22, 4 )
        h, t= dht.read_retry( dht.AM2302, 4 )
        f_h = float(h)
        if t is not None and h is not None:
            if f_h<100:
                logging.info('Temp={0:0.1f}C and Humidity={1:0.1f}%'.format(t, h))
                print( round(t, 2), round(h, 2))
                break

run_collection()
