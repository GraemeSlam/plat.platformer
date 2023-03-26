import pygame
from animate import *
from random import randint
from settings import path
import os
MushSheet = Spritesheet(os.path.join(path+"Mushroom_sheet.png"))
BounceSheet = Spritesheet(os.path.join(path+"Bounce_Mushroom_sheet.png"))
class tile (pygame.sprite.Sprite):
	def __init__(self, pos, size, spr):
		super(tile, self).__init__()
		self.spr = spr
		self.intangible = False
		self.semisolid = False
		self.fluid = False
		self.coin = False
		self.onewayl = False
		self.image = pygame.image.load(path+"empty.png")
		if self.spr == ".":
			self.intangible = True
		if self.spr == "3":
			self.image = pygame.image.load(path+"bronzepaw.png")
			self.coin = True
			self.intangible = True
			self.value = 10
		if self.spr == "4":
			self.image = pygame.image.load(path+"silverpaw.png")
			self.coin = True
			self.intangible = True
			self.value = 100
		if self.spr == "5":
			self.image = pygame.image.load(path+"goldpaw.png")
			self.coin = True
			self.intangible = True
			self.value = 1000
		elif self.spr == "d":
			self.image = pygame.image.load(path+"dirtblock.png")
		elif self.spr == "D":
			self.image = pygame.image.load(path+"dirtback.png")
			self.intangible = True
		elif self.spr == "g":
			self.image = pygame.image.load(path+"grassblock.png")
		elif self.spr == "2":
			self.image = pygame.image.load(path+"stump.png")
			self.intangible = True
		elif self.spr == "M":
			self.image = BounceSheet.get_sprite(32, 0, 30, 32)
			self.counter = 0
			self.Maxtime = randint(60, 600)
			self.active = True
		elif self.spr == "W":
			self.image = pygame.image.load(path+"Mushroom_Warrior.png")
		elif self.spr == "m":
			self.image = MushSheet.get_sprite(16*randint(0,5), 0, 15, 16)
			self.intangible = True
		elif self.spr == "q":
			self.image = pygame.image.load(path+"QuartzFloor.png")
		elif self.spr == "p":
			self.image = pygame.image.load(path+"QuartzPillar.png")
			self.intangible = True
		elif self.spr == "P":
			self.image = pygame.image.load(path+"QuartzPillarDark.png")
			self.intangible = True
		elif self.spr == "Q":
			self.image = pygame.image.load(path+"DecorativeQuartz.png")
		elif self.spr == "C":
			self.image = pygame.image.load(path+"QuartzChest.png")
		elif self.spr == "a":
			self.image = pygame.image.load(path+"Sand.png")
		elif self.spr == "s":
			self.image = pygame.image.load(path+"Stone.png")
		elif self.spr == "S":
			self.image = pygame.image.load(path+"stoneback.png")
			self.intangible = True
		elif self.spr == "w":
			self.image = pygame.image.load(path+"Water.png")
			self.fluid = True
			self.image.set_alpha(160)
		elif self.spr == "c":
			self.image = pygame.image.load(path+"Cloud.png")
			self.semisolid = True
			self.image.set_alpha(210)
		elif self.spr == "x":
			self.image = pygame.image.load(path+"empty.png")
		self.rect = self.image.get_rect(topleft = pos)
		if self.spr == "c":
			self.rect.inflate_ip(0, -35)
		if self.spr == "x":
			self.onewayl = True
			self.rect.inflate_ip(-35, 0)
		
	def update (self, x, y, precipitation):
		self.rect.centerx += x
		self.rect.centery += y
		if self.spr == "g" and precipitation == 2:
			self.image = pygame.image.load(path+"snowGrass.png")
		if self.spr == "2" and precipitation == 2:
			self.image = pygame.image.load(path+"snowStump.png")
		if self.spr == "M" and not self.active:
			self.counter +=1
			if self.counter == self.Maxtime:
				self.active = True
				self.counter = 0
				self.Maxtime = randint(60, 600)
				self.image = BounceSheet.get_sprite(32, 0, 30, 32)