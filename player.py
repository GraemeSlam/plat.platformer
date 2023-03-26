import pygame
from animate import *
from Clone import *
import os
from random import choice
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, path, sound
from pygame.locals import (
	K_UP,
	K_DOWN,
	K_LEFT,
	K_RIGHT,
	K_LSHIFT,
	K_RETURN,
	K_b,
	K_w,
	K_a,
	K_d,
	K_s,
	K_SPACE,
)
runsheet = Spritesheet(os.path.join(path+"dog_run_strip8_2.png"))
idlesheet = Spritesheet(os.path.join(path+"dog_idle_strip8_2.png"))
jumpsheet = Spritesheet(os.path.join(path+"dog_jump_strip8_2.png"))
telesheet = Spritesheet(os.path.join(path+"Teleport_sheet.png"))
pygame.mixer.init()
Bark1 = pygame.mixer.Sound(os.path.join(path+"Sounds/"+"Bark1.mp3"))
Bark2 = pygame.mixer.Sound(os.path.join(path+"Sounds/"+"Bark2.mp3"))
Bark3 = pygame.mixer.Sound(os.path.join(path+"Sounds/"+"Bark3.mp3"))
run = pygame.mixer.Sound(os.path.join(path+"Sounds/"+"run.mp3"))
jump = pygame.mixer.Sound(os.path.join(path+"Sounds/"+"jump.mp3"))
Bark1.set_volume(1*sound)
Bark2.set_volume(1*sound)
Bark3.set_volume(0.5*sound)
run.set_volume(0.35*sound)
jump.set_volume(0.5*sound)
barks = [Bark1, Bark2, Bark3]
class player (pygame.sprite.Sprite):
	def __init__(self, pos):
		super(player, self).__init__()
		self.xspeed = 5
		self.gravity = 0.49
		self.offset = -2
		self.health = 100
		self.paws = 0
		self.animation = 0
		self.step = 0
		self.past_keys = ""
		self.konamid = False
		self.toggleable = {"barking": False, "grounded": True, "running":False, "Dash":False}
		self.delay = {"bark": 0, "run":0, "Dash":0, "Dashing": 0}
		self.image = runsheet.get_sprite(60*0, 0, 60, 60)
		self.rect = self.image.get_rect(topleft = pos)
		self.direction = pygame.math.Vector2(0,0)
		self.rect.inflate_ip(-14, -36)

	def update(self, pressed_keys, xshift):
		
		if pressed_keys[K_UP] or pressed_keys[K_w]:
			if self.direction.y > -9 and self.toggleable["grounded"]:
				if sound:
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
		if pressed_keys[K_SPACE]and self.toggleable["Dash"]:
			self.delay["Dashing"] = 4
		if self.delay["Dashing"] > 0:
			if pressed_keys[K_UP] or pressed_keys[K_w]:
				self.direction.y = -33+self.konamid*10
				self.toggleable["Dash"] = False
				self.delay["Dash"] = 0
				self.image = pygame.image.load(path+"dog_dash.png")
				self.image = pygame.transform.rotate(self.image, 90)
			if pressed_keys[K_LEFT] or pressed_keys[K_a]:
				self.xspeed = 33-self.konamid*10
				self.toggleable["Dash"] = False
				self.delay["Dash"] = 0
				self.image = pygame.transform.flip(pygame.image.load(path+"dog_dash.png"),True, False)
				if pressed_keys[K_UP] or pressed_keys[K_w] or pressed_keys[K_DOWN] or pressed_keys[K_s]:
					self.image = pygame.transform.rotate(self.image, -45)
			if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
				self.xspeed = 33-self.konamid*10
				self.toggleable["Dash"] = False
				self.delay["Dash"] = 0
				self.image = pygame.image.load(path+"dog_dash.png")
				if pressed_keys[K_UP] or pressed_keys[K_w] or pressed_keys[K_DOWN] or pressed_keys[K_s]:
					self.image = pygame.transform.rotate(self.image, 45)
			if pressed_keys[K_DOWN] or pressed_keys[K_a]:
				self.direction.y = 33-self.konamid*10
				self.toggleable["Dash"] = False
				self.delay["Dash"] = 0
				self.image = pygame.image.load(path+"dog_dash.png")
				self.image = pygame.transform.rotate(self.image, -90)
			self.delay["Dashing"] -=1
		if self.delay["Dash"] > 0 and not self.toggleable["Dash"]:
			self.delay["Dash"]+=1
			if self.delay["Dash"] >= 46:
				self.toggleable["Dash"] = True
		if pressed_keys[K_b] and not self.toggleable["barking"]:
			if sound:
				pygame.mixer.Sound.play(choice(barks))
			self.toggleable["barking"] = True
			self.delay["bark"] = 0
		if self.toggleable["barking"]:
			if self.delay["bark"] >= 20:
				self.toggleable["barking"] = False
			self.delay["bark"]+=1
		if self.rect.bottom >= SCREEN_HEIGHT-50:
			self.rect.bottom = SCREEN_HEIGHT-50 
		if self.delay["Dashing"] <= 0:
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
		
		if round(self.direction.x) != 0 and self.toggleable["grounded"]and (self.direction.x > 0 or xshift < 0):
			self.image = runsheet.get_sprite(60*round(self.animation)+7, 28, 40, 30)
		elif round(self.direction.x) != 0 and self.toggleable["grounded"] and (self.direction.x < 0 or xshift > 0):
			self.image = pygame.transform.flip(runsheet.get_sprite(60*round(self.animation)+7, 28, 40, 30),True, False)
		
		elif round(self.direction.x) == 0 and self.toggleable["grounded"]:
			self.image = idlesheet.get_sprite(60*round(self.animation)+7, 28, 37, 28)
			#self.image = telesheet.get_sprite(51*round(self.animation), 0, 52, 52)
		if round(self.direction.x) != 0:
			if not self.toggleable["running"] and self.toggleable["grounded"]:
				self.toggleable["running"] = True
				self.delay["run"] = 0
				if sound:
					pygame.mixer.Sound.play(run)
			elif self.delay["run"] >= 10:
				self.toggleable["running"] = False
			else:
				self.delay["run"] += 1
		if pressed_keys[K_LSHIFT]:
			self.animation+=0.7
		else:
			self.animation+=0.5
		if self.animation > 7 and self.toggleable["grounded"]:
			self.animation = 0
		if self.animation > 7 and not self.toggleable["grounded"]:
			self.animation = 7
		#self.rect.y += self.gravity
		#self.gravity += abs(self.gravity/10)+0.1
		if self.direction.y > 15 and not self.delay["Dashing"]:
			self.direction.y = 15
		if pressed_keys[K_UP] or pressed_keys[K_DOWN] or pressed_keys[K_LEFT] or pressed_keys[K_RIGHT]or pressed_keys[K_b] or pressed_keys[K_a]or pressed_keys[K_RETURN]:
			self.konami(pressed_keys)
		if self.rect.left < 0:	
			self.rect.left = 0
		if self.rect.right > SCREEN_WIDTH:
			self.rect.right = SCREEN_WIDTH
		if self.rect.top <= 0:
			self.rect.top = 0
		if self.rect.bottom >= SCREEN_HEIGHT:
			self.rect.bottom = SCREEN_HEIGHT
	def konami(self, pressed_keys):
		if pressed_keys[K_UP] and self.step == 0:
			self.step=1
		elif pressed_keys[K_UP] and self.step == 1:
			self.step=2
		elif pressed_keys[K_DOWN] and self.step == 2:
			self.step=3
		elif pressed_keys[K_DOWN] and self.step == 3:
			self.step=4
		elif pressed_keys[K_LEFT] and self.step == 4:
			self.step=5
		elif pressed_keys[K_RIGHT] and self.step == 5:
			self.step=6
		elif pressed_keys[K_LEFT] and self.step == 6:
			self.step=7
		elif pressed_keys[K_RIGHT] and self.step == 7:
			self.step=8
		elif pressed_keys[K_b] and self.step == 8:
			self.step=9
		elif pressed_keys[K_a] and self.step == 9:
			self.step=10
		elif pressed_keys[K_RETURN] and self.step == 10:
			self.konamid = 1
		#else:
			#self.step = 0
		if self.konamid:
			self.delay["Dashing"] = 20