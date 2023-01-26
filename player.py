import pygame
from animate import *
from settings import path
import os
from random import choice
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from pygame.locals import (
	K_UP,
	K_DOWN,
	K_LEFT,
	K_RIGHT,
	K_LSHIFT,
	K_b,
	K_w,
	K_a,
	K_d,
	K_SPACE,
)
runsheet = Spritesheet(os.path.join(path+"dog_run_strip8_2.png"))
idlesheet = Spritesheet(os.path.join(path+"dog_idle_strip8_2.png"))
jumpsheet = Spritesheet(os.path.join(path+"dog_jump_strip8_2.png"))
pygame.mixer.init()
Bark1 = pygame.mixer.Sound(os.path.join(path+"Sounds/"+"Bark1.mp3"))
Bark2 = pygame.mixer.Sound(os.path.join(path+"Sounds/"+"Bark2.mp3"))
Bark3 = pygame.mixer.Sound(os.path.join(path+"Sounds/"+"Bark3.mp3"))
run = pygame.mixer.Sound(os.path.join(path+"Sounds/"+"run.mp3"))
jump = pygame.mixer.Sound(os.path.join(path+"Sounds/"+"jump.mp3"))
run.set_volume(0.25)
jump.set_volume(0.5)
barks = [Bark1, Bark2, Bark3]

class player (pygame.sprite.Sprite):
	def __init__(self, pos):
		super(player, self).__init__()
		self.xspeed = 5
		self.yspeed = 5
		self.gravity = 0.49
		self.offset = -2
		self.health = 100
		self.paws = 0
		self.animation = 0
		self.toggleable = {"barking": False, "grounded": True, "running":False}
		self.delay = {"bark": 0, "run":0}
		self.image = runsheet.get_sprite(60*0, 0, 60, 60)
		self.rect = self.image.get_rect(topleft = pos)
		self.direction = pygame.math.Vector2(0,0)
		self.rect.inflate_ip(-14, -36)
	def update(self, pressed_keys):
		
		if pressed_keys[K_UP] or pressed_keys[K_w] or pressed_keys[K_SPACE]:
			if self.direction.y > -9 and self.toggleable["grounded"]:
				pygame.mixer.Sound.play(jump)
				self.direction.y = -9
				self.animation = 0
				self.toggleable["grounded"] = False
		if pressed_keys[K_LEFT] or pressed_keys[K_a]:
			self.direction.x= -1
		elif pressed_keys[K_RIGHT] or pressed_keys[K_d]:
			self.direction.x = 1
		elif self.direction.x >= -1 and self.direction.x <= 1: 
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
		if pressed_keys[K_b] and not self.toggleable["barking"]:
			pygame.mixer.Sound.play(choice(barks))
			self.toggleable["barking"] = True
			self.delay["bark"] = 0
		if self.toggleable["barking"]:
			if self.delay["bark"] >= 20:
				self.toggleable["barking"] = False
			self.delay["bark"]+=1
		if self.rect.bottom >= SCREEN_HEIGHT-50:
			self.rect.bottom = SCREEN_HEIGHT-50 
			
		if self.direction.x > 0 and not self.toggleable["grounded"]:
			self.image = jumpsheet.get_sprite(60*round(self.animation)+7, 28, 40, 30)
			self.image = pygame.transform.rotate(self.image, self.direction.y*-3)
		if self.direction.x == 0 and not self.toggleable["grounded"]:
			self.image = jumpsheet.get_sprite(60*round(self.animation)+7, 28, 40, 30)
			pygame.transform.rotate(self.image, 45)
		self.image = pygame.transform.rotate(self.image, self.direction.y*-4)
		if self.direction.x < 0 and not self.toggleable["grounded"]:
			self.image = pygame.transform.flip(jumpsheet.get_sprite(60*round(self.animation)+7, 28, 40, 30),True, False)
			pygame.transform.rotate(self.image, 45)
			self.image = pygame.transform.rotate(self.image, self.direction.y*4)
		
		if round(self.direction.x) != 0 and self.direction.x > 0 and self.toggleable["grounded"]:
			self.image = runsheet.get_sprite(60*round(self.animation)+7, 28, 40, 30)
		elif round(self.direction.x) != 0 and self.direction.x < 0 and self.toggleable["grounded"]:
			self.image = pygame.transform.flip(runsheet.get_sprite(60*round(self.animation)+7, 28, 40, 30),True, False)
		
		elif round(self.direction.x) == 0 and self.toggleable["grounded"]:
			self.image = idlesheet.get_sprite(60*round(self.animation)+7, 28, 37, 28)
		if round(self.direction.x) != 0:
			if not self.toggleable["running"] and self.toggleable["grounded"]:
				self.toggleable["running"] = True
				self.delay["run"] = 0
				pygame.mixer.Sound.play(run)
			elif self.delay["run"] >= 10:
				self.toggleable["running"] = False
			else:
				self.delay["run"] += 1
		self.animation+=0.5
		if self.animation > 7 and self.toggleable["grounded"]:
			self.animation = 0
		if self.animation > 7 and not self.toggleable["grounded"]:
			self.animation = 7
		#self.rect.y += self.gravity
		#self.gravity += abs(self.gravity/10)+0.1
		if self.direction.y > 15:
			self.direction.y = 15
		