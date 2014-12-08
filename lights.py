import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def switch(channel):
    
    print "SWITCHING " + str(channel)
    GPIO.setup(channel,GPIO.OUT)
    time.sleep(1)
    GPIO.setup(channel,GPIO.IN)

def test():
    
    channels = [(22,21),(27,20),(17,12)]

    for channelPair in channels:
        switch(channelPair[0])
        time.sleep(5)
        switch(channelPair[1])

    GPIO.cleanup()

if __name__ == "__main__":
    test()
    
