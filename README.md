#raspberry_pi_led

This repository contains basic functionality for communication with the Raspberry Pi GPIO interface. This code is all experimental and requires that the Pi is wired in the correct manor.

##Overview

######GPIO Out

Defines a class to interact with a number of GPIO outputs. After initialisation with a list of GPIO pin numbers a list of on/off (True/False) Bool values can be passed to a method of the class to control all the outputs.

######GPIO In

Defines a class to interact with a single GPIO input. After initialisation with a single GPIO pin number the method listen can be called to return when the button is pressed.

######Flash LED

Simple script to cause a single LED to flash in a series of long and short flashes.

######Binary Counter

Contains functions to output a binary count from 0 to 15 on 4 LEDs. The count is incremented each time the input button is depressed.

##Licence

Please feel free to use this code however you wish so long as its solely for personal use and credit is given to myself.