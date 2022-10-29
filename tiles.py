import pygame
from animate import *
from random import randint
import os
MushSheet = Spritesheet(os.path.join("Mushroom_sheet.png"))
BounceSheet = Spritesheet(os.path.join("Bounce_Mushroom_sheet.png"))
class tile (pygame.sprite.Sprite):
	def __init__(self, pos, size, spr):
		super(tile, self).__init__()
		self.spr = spr
		self.image = pygame.image.load("empty.png")
		if self.spr == 0:
			self.image = pygame.image.load("dirtblock.png")
		elif self.spr == 1:
			self.image = pygame.image.load("grassblock.png")
		elif self.spr == 3:
			self.image = MushSheet.get_sprite(16*randint(0,5), 0, 15, 16)
			print("Mush")
		elif self.spr == 4:
			self.image = BounceSheet.get_sprite(30, 0, 32, 32)
		self.rect = self.image.get_rect(topleft = pos)
		
	def update (self, x, y):
		self.rect.x += x
		self.rect.y += y