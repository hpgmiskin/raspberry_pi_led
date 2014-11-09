import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class gpioIn():
	"""gpioIn provides an interface for a single input from the GPIO"""

	def __init__(self,pin):
		"Sets pin attribute and calls setup"
		self.pin = pin;
		self.setupPin();

	def setupPin(self):
		"Setup GPIO input pin"
		GPIO.setup(self.pin,GPIO.IN)

	def listen(self):
		"Listen for key press"

		while True:
			input = GPIO.input(self.pin)
			if input:
				return
			time.sleep(0.01)