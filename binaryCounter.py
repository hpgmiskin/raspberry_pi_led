import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def decimalBinary(decimal):
	""" 4 bit decimal to binary converter """

	binaryPLaceholders = [8,4,2,1]
	binary = []

	for placeholder in binaryPLaceholders:

		if (decimal >= placeholder):
			decimal = decimal - placeholder
			binary.append(1)
		else:
			binary.append(0)

	return binary

def binaryCounter():
	""" function to count between 0 and 15 in binary """

	outPins = gpioOut([25,24,23,18])

	for decimal in range(16):
		binary = decimalBinary(decimal)
		outPins.switchPins(binary)
		print("{} - {}".format(decimal,binary))
		time.sleep(0.5)

	outPins.switchPins([0,0,0,0])


class gpioOut():
	"""docstring for gpioOut"""

	def __init__(self, pins):
		self.pins = pins
		self.setupPins()

	def setupPins(self):
		for pin in self.pins:
		 	GPIO.setup(pin,GPIO.OUT)

	def switchPins(self,logicList):
		assert(len(logicList) == len(self.pins))

		for i,logic in enumerate(logicList):
			self.switchPin(self.pins[i],logic)

	def switchPin(self,pin,logic):
		if logic:
			self.turnOn(pin)
		else:
			self.turnOff(pin)

	def turnOn(self,pin):
	 	GPIO.output(pin,GPIO.HIGH)

	def turnOff(self,pin):
	 	GPIO.output(pin,GPIO.LOW)

		

if __name__ == "__main__":
	binaryCounter()

