#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import curses
import sys
import time
import smbus

delay = 1;

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

    # Shake gets rid of everything on the screen
    def shake(self):
        self.height, self.width = [8, 8]
        for y in range(0, self.height):
            for x in range(0, self.width):
                try:
                    self.stdscr.addstr(y, x, self.empty)
                except curses.error:
                    pass
    # This is the cursor function which writes to a position
    def cursor(self):
        try:
            self.stdscr.addstr(self.pos[1], self.pos[0], self.cursorc)
        except curses.error:
            pass

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
        # Setting up the LED matrix
        bus = smbus.SMBus(2)  # Use i2c bus 1
        matrix = 0x70         # Use address 0x70
        bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
        bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
        bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)
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
                if GPIO.input(buttonUp):
                    if self.pos[1] > 0:
                        self.pos[1] -= 1
                elif GPIO.input(buttonDown):
                    if self.pos[1] < self.height - 1:
                        self.pos[1] += 1
                elif GPIO.input(buttonLeft):
                    if self.pos[0] > 0:
                        self.pos[0] -= 1
                elif GPIO.input(buttonRight):
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
                # Draw something on the board
                stdscr.addstr(self.oldpos[1], self.oldpos[0], self.full)
                # Update the old position
                self.oldpos = list(self.pos)
                time.sleep(delay/10)
        finally:
              GPIO.cleanup()

sketch = Sketch()
curses.wrapper(sketch.main)
