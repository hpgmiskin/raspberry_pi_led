import time
import RPi.GPIO as GPIO

def flash():

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(25, GPIO.OUT)

    delay = 0.1

    for i in range(20):
        GPIO.output(25, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(25, GPIO.LOW)
        time.sleep(delay)

if __name__ == "__main__":
    flash()
