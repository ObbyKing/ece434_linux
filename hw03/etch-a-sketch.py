#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import curses
import sys
import time
import smbus
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP1, eQEP2

delay = 2

class Sketch(object):
    def __init__(self):
        # (X, Y)
        self.pos = [0, 0]
        self.oldpos = list(self.pos)
        self.height = 0
        self.width = 0
        # Declare what I want the board to look like
        self.full = "X"
        self.empty = " "
        self.cursorc = "O"
        self.stdscr = None
        self.ledState = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        self.matrix = 0x70
        self.bus = smbus.SMBus(2)

    # Shake gets rid of everything on the screen
    def shake(self):
        self.height, self.width = [8, 8]
        for y in range(0, self.height):
            for x in range(0, self.width):
                try:
                    self.stdscr.addstr(y, x, self.empty)
                except curses.error:
                    pass
        for x in range (0, len(self.ledState)):
                self.ledState[x] = 0x00
        self.bus.write_i2c_block_data(self.matrix, 0, self.ledState)
    # This is the cursor function which writes to a position
    def cursor(self):
        try:
            self.stdscr.addstr(self.pos[1], self.pos[0], self.cursorc)
            currentStateRed = self.ledState[(self.pos[0]*2)+1]
            self.ledState[(self.pos[0]*2)+1] = currentStateRed | (1 << self.pos[1])
            self.bus.write_i2c_block_data(self.matrix, 0, self.ledState)
        except curses.error:
            pass

    def updateLEDMatrix(self):
        currentStateGreen = self.ledState[(self.oldpos[0]*2)]
        self.ledState[(self.oldpos[0]*2)] = currentStateGreen | (1 << self.oldpos[1])
        currentStateRed = self.ledState[(self.oldpos[0]*2)+1]
        self.ledState[(self.oldpos[0]*2)+1] = 0x00
        self.bus.write_i2c_block_data(self.matrix, 0, self.ledState)

    def main(self, stdscr):
        # Defining Buttons
        buttonUp = "P9_27"
        buttonDown = "P9_16"
        buttonLeft = "P9_17"
        buttonRight = "P9_18"
        buttonQuit = "P9_22"
        buttonShake = "P9_24"
        # Setting up buttons
        GPIO.setup(buttonUp, GPIO.IN)
        GPIO.setup(buttonDown, GPIO.IN)
        GPIO.setup(buttonLeft, GPIO.IN)
        GPIO.setup(buttonRight, GPIO.IN)
        GPIO.setup(buttonQuit, GPIO.IN)
        GPIO.setup(buttonShake, GPIO.IN)
        # Setup the encoders
        upDownEncoder = RotaryEncoder(eQEP2)
        leftRightEncoder = RotaryEncoder(eQEP1)
        upDownEncoder.setAbsolute()
        leftRightEncoder.setAbsolute()
        upDownEncoder.enable()
        leftRightEncoder.enable()
        # Setting up the LED matrix
        self.bus.write_byte_data(self.matrix, 0x21, 0)   # Start oscillator (p10)
        self.bus.write_byte_data(self.matrix, 0x81, 0)   # Disp on, blink off (p11)
        self.bus.write_byte_data(self.matrix, 0xe7, 0)   # Full brightness (page 15)
        # Pointing the screen to itself
        self.stdscr = stdscr
        stdscr.clear()
        self.shake()
        try:
            while True:
                # Update cursor
                self.cursor()
                # Initliaze the screen
                curses.initscr()
                if GPIO.input(buttonUp) | upDownEncoder.position > 0:
                    if self.pos[1] > 0:
                        self.pos[1] -= 1
                elif GPIO.input(buttonDown) | upDownEncoder.position < 0:
                    if self.pos[1] < self.height - 1:
                        self.pos[1] += 1
                elif GPIO.input(buttonLeft) | leftRightEncoder.position > 0:
                    if self.pos[0] > 0:
                        self.pos[0] -= 1
                elif GPIO.input(buttonRight) | leftRightEncoder.position < 0:
                    if self.pos[0] < self.width - 1:
                        self.pos[0] += 1
                elif GPIO.input(buttonQuit):
                    break
                elif GPIO.input(buttonShake):
                    self.shake()
                    self.oldpos = list(self.pos)
                    continue
                else:
                    continue
                upDownEncoder.position = 0
                leftRightEncoder.position = 0
                # Draw something on the board
                stdscr.addstr(self.oldpos[1], self.oldpos[0], self.full)
                self.updateLEDMatrix()
                # Update the old position
                self.oldpos = list(self.pos)
                time.sleep(delay/10)
        finally:
              GPIO.cleanup()

sketch = Sketch()
curses.wrapper(sketch.main)
