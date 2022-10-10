import pygame, sys
from settings import *
from tiles import tile 
from level import *
from player import *
from pygame.locals import (
	QUIT,
)
pygame.init()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
testlevel = level(level0, screen)
clock = pygame.time.Clock() 
running = True

while running:
	clock.tick (30)
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
	screen.fill((0, 105, 155))
	pressed_keys = pygame.key.get_pressed()
	testlevel.collide()
	testlevel.player.update(pressed_keys)
	testlevel.loadlevel()
	pygame.display.update()
pygame.quit()
sys.exit()