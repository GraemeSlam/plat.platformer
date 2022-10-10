import pygame
class tile (pygame.sprite.Sprite):
	def __init__(self, pos, size, spr):
		super(tile, self).__init__()
		self.spr = spr
		self.image = pygame.image.load("empty.png")
		if self.spr == 0:
			self.image = pygame.image.load("dirtblock.png")
		elif self.spr == 1:
			self.image = pygame.image.load("grassblock.png")
		self.rect = self.image.get_rect(topleft = pos)
	def update (self, x, y):
		self.rect.x += x
		self.rect.y += y