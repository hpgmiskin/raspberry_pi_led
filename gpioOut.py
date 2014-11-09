import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class gpioOut():
	"""gpioOut contains the functionality to output to any number of GPIO pins"""

	def __init__(self, pins):
		"Set pins attribute and call setup"
		
		self.pins = pins
		self.setupPins()

	def setupPins(self):
		"Setup all pins constructed"

		for pin in self.pins:
		 	GPIO.setup(pin,GPIO.OUT)

	def switchPins(self,onOffList):
		"Switch all pins based on list of bool onOff values"

		#make sure onOffList is same length as pins
		assert(len(onOffList) == len(self.pins))

		for i,onOff in enumerate(onOffList):
			self.switchPin(self.pins[i],onOff)

	def switchPin(self,pin,onOff):
		"Switch the given pin on or off depending on bool onOff"

		if onOff:
			self.turnOn(pin)
		else:
			self.turnOff(pin)

	def turnOn(self,pin):
		"Turn given pin on"
		GPIO.output(pin,GPIO.HIGH)

	def turnOff(self,pin):
		"Turn given pin off"
		GPIO.output(pin,GPIO.LOW)
