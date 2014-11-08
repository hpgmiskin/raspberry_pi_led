import time
import RPi.GPIO as GPIO

def flash():

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(25, GPIO.OUT)

    delays = [1,0.2]*10

    for delay in delays:
        GPIO.output(25, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(25, GPIO.LOW)
        time.sleep(0.5)

if __name__ == "__main__":
    flash()
