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

	for i in range(16):
		binary = decimalBinary(i)
		outPins.switchPins(binary)
		print("{} - {}".format(decimal,binary))
		time.sleep(0.5)


class gpioOut():
	"""docstring for gpioOut"""

	def __init__(self, pins):
		self.pins = pins
		self.setupPins()

	def setupPins():
		for pin in self.pins:
			GPIO.setup(pin,GPIO.OUT)

	def switchPins(logicList):
		assert(length(logicList) == length(self.pins))

		for i,logic in enumerate(logicList):
			self.switchPin(self.pins[i],logic)

	def switchPin(pin,logic):
		if logic:
			self.turnOn(pin)
		else:
			self.turnOff(pin)

	def turnOn(pin):
		GPIO.output(pin,GPIO.HIGH)

	def turnOff(pin):
		GPIO.output(pin,GPIO.HIGH)
		

if __name__ == "__main__":
	print(decimalBinary(15))
	print(decimalBinary(8))
	print(decimalBinary(7))

