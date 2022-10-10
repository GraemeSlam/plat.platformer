import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from pygame.locals import (
	K_UP,
	K_DOWN,
	K_LEFT,
	K_RIGHT,
	K_LSHIFT
)
class player (pygame.sprite.Sprite):
	def __init__(self, pos):
		super(player, self).__init__()
		self.xspeed = 5
		self.yspeed = 5
		self.gravity = 0.7
		self.health = 100
		self.image = pygame.image.load("dog.png")
		self.rect = self.image.get_rect(topleft = pos)
		self.direction = pygame.math.Vector2(0,0)
	def update(self, pressed_keys):
		
		if pressed_keys[K_UP]:
			self.direction.y = -9
		'''
		else: 
			self.direction.y = 0
		'''
		if pressed_keys[K_LEFT]:
			self.direction.x= -1
		elif pressed_keys[K_RIGHT]:
			self.direction.x = 1
		else: 
			self.direction.x = 0
		if self.direction.x == 0:
			if pressed_keys[K_LSHIFT]:
				self.speed = 10
			else:	
				self.speed = 5
		'''
		if self.direction.y == 0:
			self.yspeed = 10
		else:
			pass
		if self.gravity < 0:
			self.direction.y= -1
		elif self.gravity > 0:
			self.direction.y= 1
	    '''
		#self.rect.y += self.gravity
		#self.gravity += abs(self.gravity/10)+0.1
		self.direction.y += self.gravity
		self.rect.x+= self.direction.x*self.xspeed
		self.rect.y+= self.direction.y