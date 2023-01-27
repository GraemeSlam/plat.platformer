import pygame
from settings import path, SCREEN_WIDTH, SCREEN_HEIGHT
import random
class rain(pygame.sprite.Sprite):
	def __init__(self):
		super(rain, self).__init__()

		self.speed = random.randint(7, 12)
		self.image = pygame.image.load(path+"RainDrop.png")
		self.image.set_alpha(170)
		self.rect = self.image.get_rect(
			center=(
					random.randint(0, SCREEN_WIDTH),
					-2
				)
		)	
		
	def update(self):	
		self.rect.move_ip(0, self.speed)
		if self.rect.top < 0:	
			self.kill()