import time
from gpioIn import gpioIn
from gpioOut import gpioOut

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

	inPin = gpioIn(20)
	outPins = gpioOut([25,24,23,18])

	for decimal in range(16):
		binary = decimalBinary(decimal)
		outPins.switchPins(binary)
		print("{} - {}".format(decimal,binary))
		inPin.listen()
		time.sleep(0.5)

	outPins.switchPins([0,0,0,0])		

if __name__ == "__main__":
	binaryCounter()

