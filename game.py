import pygame, sys
from settings import *
from tiles import tile 
from level import *
from player import *
from Rain import *
from pygame.locals import (
	QUIT,
)
pygame.init()
pygame.font.init()
paw = pygame.image.load(path+"goldpaw.png")
splashfx = pygame.image.load(path+"rainsplash.png")
retro = pygame.font.Font(path+"A Goblin Appears!.otf", 17)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
level1 = level(level1, screen)
clock = pygame.time.Clock() 
rains = pygame.sprite.Group()
running = True
Background = pygame.image.load(Backgrounds[1])
ADDRAIN = pygame.USEREVENT + 1
pygame.time.set_timer(ADDRAIN, 10)
pygame.mixer.music.load(os.path.join(path+"Sounds/"+"drip.mp3"))
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play(-1)



while running:
	clock.tick (30)
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
	screen.fill((0, 105, 155))
	if level1.precipitation: 
		Background = pygame.image.load(Backgrounds[1+(level1.precipitation/10)])
		
	else:
		Background = pygame.image.load(Backgrounds[1])
		pygame.mixer.music.pause()
	if level1.precipitation == 1:
		pygame.mixer.music.unpause()
	if level1.precipitation == 2:
		pygame.mixer.music.pause()
	screen.blit(Background, (0,0))
	pressed_keys = pygame.key.get_pressed()
	if event.type == ADDRAIN and level1.precipitation:
		new_rain = rain(level1.precipitation)
		rains.add(new_rain)
	level1.player.update(pressed_keys, level1.xshift)
	level1.loadlevel(pressed_keys)
	if level1.player.sprite.paws > 999:
		money = retro.render(str(level1.player.sprite.paws), False, (255,255,255))
	elif level1.player.sprite.paws > 99:
		money = retro.render("0"+str(level1.player.sprite.paws), False, (255,255,255))
	elif level1.player.sprite.paws > 9:
		money = retro.render("00"+str(level1.player.sprite.paws), False, (255,255,255))
	elif level1.player.sprite.paws < 10:
		money = retro.render("000"+str(level1.player.sprite.paws), False, (255,255,255))
	rains.update(level1.xshift/2)
	for entity in rains:
		screen.blit(entity.image, entity.rect)
	splash = pygame.sprite.groupcollide(rains, level1.tiles, True, 
	False)
	splash1 = pygame.sprite.groupcollide(rains, level1.player, True, 
	False)
	splash = list(splash.keys())
	splash1 = list(splash1.keys())

	if (splash or splash1) and level1.precipitation == 1:
		for thing in splash:
			screen.blit(splashfx, thing.rect.center)
		for thing in splash1:
			screen.blit(splashfx, thing.rect.center)
		
	screen.blit(money, (730, 5))
	screen.blit(paw, (705, 5))
	pygame.display.update()
pygame.quit()
sys.exit()