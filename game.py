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
testlevel = level(level1, screen)
clock = pygame.time.Clock() 
running = True
Background = pygame.image.load(Backgrounds[1])
while running:
	clock.tick (30)
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
	screen.fill((0, 105, 155))
	screen.blit(Background, (0,0))
	pressed_keys = pygame.key.get_pressed()
	testlevel.player.update(pressed_keys)
	testlevel.loadlevel(pressed_keys)
	pygame.display.update()
pygame.quit()
sys.exit()