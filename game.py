import pygame, sys
from settings import *
from tiles import tile 
from level import *
from player import *
from pygame.locals import (
	QUIT,
)
pygame.init()
pygame.font.init()
paw = pygame.image.load(path+"goldpaw.png")
retro = pygame.font.Font(path+"A Goblin Appears!.otf", 17)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
level1 = level(level1, screen)
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
	level1.player.update(pressed_keys)
	level1.loadlevel(pressed_keys)
	if level1.player.sprite.paws > 999:
		money = retro.render(str(level1.player.sprite.paws), False, (255,255,255))
	elif level1.player.sprite.paws > 99:
		money = retro.render("0"+str(level1.player.sprite.paws), False, (255,255,255))
	elif level1.player.sprite.paws > 9:
		money = retro.render("00"+str(level1.player.sprite.paws), False, (255,255,255))
	elif level1.player.sprite.paws < 10:
		money = retro.render("000"+str(level1.player.sprite.paws), False, (255,255,255))
	screen.blit(money, (730, 5))
	screen.blit(paw, (705, 5))
	pygame.display.update()
pygame.quit()
sys.exit()