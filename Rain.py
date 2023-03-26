import pygame
from settings import path, SCREEN_WIDTH, SCREEN_HEIGHT
import random
import os
#drip.set_volume(0.25)
class rain(pygame.sprite.Sprite):
	def __init__(self, precipitation):
		self.animation = 0
		self.lag = False
		super(rain, self).__init__()
		self.precipitation = precipitation
		if self.precipitation == 1:
			self.speed = random.randint(7, 12)
		elif self.precipitation == 2:
			self.speed = random.randint(5, 6)
			
		if self.precipitation == 1:
			self.image = pygame.image.load(path+"RainDrop.png")
		elif self.precipitation == 2:
			self.image = pygame.image.load(path+"snow.png")
			
		self.rect = self.image.get_rect(
			center=(
					random.randint(0, SCREEN_WIDTH),
					-2
				)
		)	
	def update(self, xshift):	
		self.rect.x+= xshift
		self.rect.y+= self.speed
		if self.rect.top < 0:	
			self.kill()
		if self.rect.left > SCREEN_WIDTH:	
			self.rect.right = 0
		elif self.rect.right < 0:	
			self.rect.left = SCREEN_WIDTH
		if self.precipitation == 2:
			if self.animation <5 and not self.lag:
				self.image = pygame.image.load(path+"snow.png")
				self.animation += 0.5
			if self.animation >= 5 and not self.lag:
				self.image = pygame.image.load(path+"snow2.png")
				pass
		if self.animation >= 10:
			self.animation = 0