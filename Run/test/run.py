import Adafruit_DHT as dht
import logging
import time


#logging.basicConfig( filename='./Temp_Humi.log', filemode='a', format='%(created)f %(message)s', level=logging.INFO)


def run_collection():
    while True:
        h, t= dht.read_retry( dht.AM2302, 4 )
        print( t, h)
        break
        #time.sleep(1)
        #if t is not None and h is not None:
        #    #logging.info('Temp={0:0.1f}C and Humidity={1:0.1f}%'.format(t, h))
        #    print( t, h)
        #    time.sleep(1)

run_collection()
