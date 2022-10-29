import pygame
from animate import *
import os
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from pygame.locals import (
	K_UP,
	K_DOWN,
	K_LEFT,
	K_RIGHT,
	K_LSHIFT
)
runsheet = Spritesheet(os.path.join("dog_run_strip8_2.png"))
idlesheet = Spritesheet(os.path.join("dog_idle_strip8_2.png"))
jumpsheet = Spritesheet(os.path.join("dog_jump_strip8_2.png"))
class player (pygame.sprite.Sprite):
	def __init__(self, pos):
		super(player, self).__init__()
		self.xspeed = 5
		self.yspeed = 5
		self.gravity = 0.7
		self.offset = -2
		self.health = 100
		self.animation = 0
		self.image = runsheet.get_sprite(60*0, 0, 60, 60)
		self.rect = self.image.get_rect(topleft = pos)
		self.direction = pygame.math.Vector2(0,0)
		self.rect.inflate_ip(-14, -36)
	def update(self, pressed_keys):
		
		if pressed_keys[K_UP] and self.direction.y > -9:
			self.direction.y = -9
			self.animation = 0
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
		if round(self.direction.y) != 0:
			self.image = jumpsheet.get_sprite(60*round(self.animation)+7, 28, 40, 30)
			print("jump")
		if round(self.direction.x) != 0 and self.direction.x > 0:
			self.image = runsheet.get_sprite(60*round(self.animation)+7, 28, 40, 30)
		elif round(self.direction.x) != 0 and self.direction.x < 0:
			self.image = pygame.transform.flip(runsheet.get_sprite(60*round(self.animation)+7, 28, 40, 30),True, False)
		elif round(self.direction.x) == 0 :
			self.image = idlesheet.get_sprite(60*round(self.animation)+7, 28, 37, 28)
		self.animation+=0.5
		if self.animation > 7:
			self.animation = 0
		#self.rect.y += self.gravity
		#self.gravity += abs(self.gravity/10)+0.1
		self.direction.y += self.gravity
		self.rect.x+= self.direction.x*self.xspeed
		self.rect.y+= self.direction.y