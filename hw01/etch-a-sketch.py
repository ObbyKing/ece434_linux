#!/usr/bin/env python

#######################
# Name: Andrew Lund
# CM: 2477
# Date: 9/6/18
#######################

import pygame, sys
from pygame.locals import *

# Initialize instance of pygame
pygame.init()

# Make a screen object for pygame
screen = pygame.display.set_mode((1280,720))

# Starting position of the cursor
x = 640
y = 360

# Set up a clock object to constantly update game state
clock = pygame.time.Clock()

# Paint the screen black
screen.fill((0,0,0))

print("Use WASD to draw")
print("Use C to clear")
print("Use the escape key to quit")

# Set up arrays for different cursor colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
pink = (255,200,200)
# Size of the cursor
circleRadius = 5

while 1:
	# Update game every 60 ms
	clock.tick(60)
	# Draw the circle
	pygame.draw.circle(screen, pink, (x,y),circleRadius)
	# Update the display
	pygame.display.update()
	# Get a key object and check to see if it is any of the drawing keys
	key = pygame.key.get_pressed()
	if key[pygame.K_d] : x += 1
	if key[pygame.K_a] : x -= 1
	if key[pygame.K_w] : y -= 1
	if key[pygame.K_s] : y += 1

	# Check other keys while looking for the movement keys.
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		# Exit if escape is pressed
		elif event.type == KEYDOWN and event.key == K_ESCAPE:
			sys.exit()
		# Clear the board if c is pressed
		elif event.type == KEYDOWN and event.key == K_c:
			screen.fill((0,0,0))