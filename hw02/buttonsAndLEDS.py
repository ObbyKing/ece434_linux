#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import time

#setup the pins
button0	= "P9_27"
button1 = "P9_16"
button2 = "P9_17"
button3 = "P9_18"
LED0	= "P9_12"
LED1	= "P9_15"
LED2	= "P9_23"
LED3	= "P9_25"

# Set the GPIO pins:
GPIO.setup(LED0, GPIO.OUT)
GPIO.setup(button0, GPIO.IN)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(button1, GPIO.IN)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(button2, GPIO.IN)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(button3, GPIO.IN)

# Turn on all LEDs
GPIO.output(LED0, 1)
GPIO.output(LED1, 1)
GPIO.output(LED2, 1)
GPIO.output(LED3, 1)

# Map buttons to LEDs
map = {button0 : LED0, button1 : LED1, button2 : LED2, button3 : LED3}

def updateLED(channel):
	print("channel = " + channel)
	state = GPIO.input(channel)
	GPIO.output(map[channel], state)
	print(map[channel] + " Toggled")

print("Running...")

GPIO.add_event_detect(button0, GPIO.BOTH, callback = updateLED)
GPIO.add_event_detect(button1, GPIO.BOTH, callback = updateLED)
GPIO.add_event_detect(button2, GPIO.BOTH, callback = updateLED)
GPIO.add_event_detect(button3, GPIO.BOTH, callback = updateLED)

try:
	while True:
		time.sleep(100)

except KeyboardInterrupt:
	print("Cleaning Up")
	GPIO.cleanup()
GPIO.cleanup()
