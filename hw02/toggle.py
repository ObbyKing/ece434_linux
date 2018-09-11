#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import time

#setup the pins
LED0	= "P9_12"

# Set the GPIO pins:
GPIO.setup(LED0, GPIO.OUT)

while 1:
	GPIO.output(LED0, GPIO.HIGH)
	time.sleep(0.000000005)
	GPIO.output(LED0, GPIO.LOW)
	time.sleep(0.000000005)
