import Adafruit_DHT as dht
import logging
import time


logging.basicConfig( filename='./Temp_Humi.log', filemode='a', format='%(created)f %(message)s', level=logging.INFO)


def run_collection():
    while True:
        print( "I ma here" )
        start = time.time()
        h, t= dht.read_retry( dht.DHT22, 4 )
        end   = time.time()
        print( 'time cost', end-start )
        if t is not None and h is not None:
            #logging.info('Temp={0:0.1f}C and Humidity={1:0.1f}%'.format(t, h))
            print( t, h)
            break

run_collection()
