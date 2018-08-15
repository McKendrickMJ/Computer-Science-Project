## - Build 1 - This build lays down the game foundations with no art or game logic.

import pygame
import random
import math

# -- Global Constants

# -- Colours
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
MAGENTA = (255,0,255)
AQUA = (0,255,255)

# -- Initialise Pygame
pygame.init()

# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)

# -- Title of Window
pygame.display.set_caption("Game")

# -- Classes

# -- Exit Game Flag Set to False
done = False

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

### -- Game Loop
while not done:
	# -- User Input and Controls
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		#End If

	# -- Game Logic

	# -- Screen Background Colour
	screen.fill(WHITE)

	# -- Draw here

	# -- Flip display to reveal new object positions
	pygame.display.flip()

	# -- Clock Speed
	clock.tick(60)

### -- End Game Loop
pygame.quit()
