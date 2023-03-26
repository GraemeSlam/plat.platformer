import pygame

class Clone:
	def __init__(self, image, starttrans, x, y): 
		self.trans= starttrans
		self.image = pygame.image.load(image)
		self.rect = self.image.get_rect(center = (x, y))
	def update(self):
		self.image.set_alpha(self.trans)
		self.image.blit(self.image,self.rect.center)
		self.trans -= 1