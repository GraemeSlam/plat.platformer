import pygame
from animate import *
from random import randint
from settings import path
import os
print(os.getcwd())
MushSheet = Spritesheet(os.path.join(path+"Mushroom_sheet.png"))
BounceSheet = Spritesheet(os.path.join(path+"Bounce_Mushroom_sheet.png"))
class tile (pygame.sprite.Sprite):
	def __init__(self, pos, size, spr):
		super(tile, self).__init__()
		self.spr = spr
		self.intangible = False
		self.semisolid = False

		self.image = pygame.image.load(path+"empty.png")
		if self.spr == ".":
			self.intangible = True
		
		elif self.spr == "d":
			self.image = pygame.image.load(path+"dirtblock.png")
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
		elif self.spr == "s":
			self.image = pygame.image.load(path+"Sand.png")
		elif self.spr == "w":
			self.image = pygame.image.load(path+"Water.png")
			self.intangible = True
		elif self.spr == "c":
			self.image = pygame.image.load(path+"Cloud.png")
			self.semisolid = True
		self.rect = self.image.get_rect(topleft = pos)
		if self.spr == "c":
			self.rect.inflate_ip(0, -35)
		
	def update (self, x, y):
		self.rect.x += x
		self.rect.y += y
		if self.spr == "M" and not self.active:
			self.counter +=1
			if self.counter == self.Maxtime:
				self.active = True
				self.counter = 0
				self.Maxtime = randint(60, 600)
				self.image = BounceSheet.get_sprite(32, 0, 30, 32)