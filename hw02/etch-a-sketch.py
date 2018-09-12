#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import curses
import sys

#setup the pins
button0	= "P9_27"
button1 = "P9_16"
button2 = "P9_17"
button3 = "P9_18"

# Set the GPIO pins:
GPIO.setup(button0, GPIO.IN)
GPIO.setup(button1, GPIO.IN)
GPIO.setup(button2, GPIO.IN)
GPIO.setup(button3, GPIO.IN)

class Sketch(object):
    def __init__(self):
        # (X, Y)
        self.pos = [0, 0]
        self.oldpos = list(self.pos)
        self.height = 0
        self.width = 0
        self.full = "X"
        self.empty = " "
        self.cursorc = "O"
        self.stdscr = None

    def shake(self):
        self.height, self.width = self.stdscr.getmaxyx()
        for y in range(0, self.height):
            for x in range(0, self.width):
                try:
                    self.stdscr.addstr(y, x, self.empty)
                except curses.error:
                    pass

    def cursor(self):
        try:
            self.stdscr.addstr(self.pos[1], self.pos[0], self.cursorc)
        except curses.error:
            pass

    def moveCursorUp(self):
	if self.pos[1] > 0:
		self.pos[1] -= 1

    def moveCursorDown(self):
	if self.pos[1] < self.height - 1:
		self.pos[1] += 1

    def moveCursorLeft(self):
        if self.pos[0] > 0:
		self.pos[0] -= 1

    def moveCursorRight(self):
	if self.pos[0] < self.width - 1:
		self.pos[0] += 1

    def main(self, stdscr):
	GPIO.add_event_detect(button0, GPIO.HIGH, callback = moveCursorUp)
	GPIO.add_event_detect(button1, GPIO.HIGH, callback = moveCursorDown)
	GPIO.add_event_detect(button2, GPIO.HIGH, callback = moveCursorLeft)
	GPIO.add_event_detect(button3, GPIO.HIGH, callback = moveCursorRight)
        self.stdscr = stdscr
        stdscr.clear()
        self.shake()
        while True:
            self.cursor()
            c = stdscr.getch(self.height - 1, self.width - 1)
            if c == ord('q'):
                break
            elif c == ord('s'):
                self.shake()
                self.oldpos = list(self.pos)
                continue
            else:
                continue
            stdscr.addstr(self.oldpos[1], self.oldpos[0], self.full)
            self.oldpos = list(self.pos)

sketch = Sketch()
curses.wrapper(sketch.main)
