import pygame
from tiles import *
from player import *
from settings import tilesize, sound
from random import randint
from pygame.locals import (
	K_r,
	K_DOWN,
	K_s,
)
ding = pygame.mixer.Sound(os.path.join(path+"Sounds/"+"ding.mp3"))
jump = pygame.mixer.Sound(os.path.join(path+"Sounds/"+"jump.mp3"))
ding.set_volume(0.5*sound)
jump.set_volume(0.5*sound)
class level:
	def __init__(self, text, screen):
		self.text = text
		self.screen = screen
		self.xshift = 0
		self.yshift = 0
		self.precipitation = 0
		self.createlevel()
		
	def createlevel(self):
		self.tiles = pygame.sprite.Group()
		self.clones = pygame.sprite.Group()
		self.player = pygame.sprite.GroupSingle()
		for row_index,row in reversed(list(enumerate(self.text))):
			for symbol_index,symbol in enumerate(row):
				x = symbol_index*tilesize
				y = row_index*tilesize-600

				if symbol == "2":
					y+=24
					Fox = player((x+5, y))
					self.player.add(Fox)
				elif symbol == "M":
					y+=8
				elif symbol == "W":
					y-=16
				elif symbol == "m":
					x+=randint(0,25)
					y+=24
				elif symbol == "w":
					y+=2
				elif symbol == "x":
					x-=17
				if not symbol == ".":
					Tile = tile((x, y), tilesize, symbol)
					self.tiles.add(Tile)
				x = symbol_index*tilesize
				y = row_index*tilesize-100
	def movex (self, pressed_keys):
		player = self.player.sprite
		if player.rect.centerx < 200 and player.direction.x < 0:
			if pressed_keys[K_LSHIFT]:
				self.xshift = 10
			elif player.konamid:
				self.xshift = 25
			else:	
				self.xshift = 8
			player.xspeed = 0
		elif player.rect.centerx > 600 and player.direction.x > 0:
			if pressed_keys[K_LSHIFT]:
				self.xshift = -10
			elif player.konamid:
				self.xshift = -25
			else:	
				self.xshift = -8
			player.xspeed = 0
		else:
			self.xshift = 0
			if pressed_keys[K_LSHIFT]:
				player.xspeed = 8
			elif player.konamid:
				player.xspeed = 25
			else:
				player.xspeed = 6
	def movey (self, pressed_keys):
		player = self.player.sprite
		if player.rect.centery < 200 and player.direction.y < 0:
			self.yshift = -player.direction.y 
		elif player.rect.centery > 500 and player.direction.y > 0:
			self.yshift = -player.direction.y
		else:
			self.yshift = 0
	def collideX(self):
		player = self.player.sprite
		player.rect.x+= player.direction.x*player.xspeed
		for rectagle in self.tiles.sprites():
			if rectagle.rect.colliderect(self.player.sprite.rect)and not rectagle.intangible and not rectagle.fluid:
				if (self.player.sprite.direction.x<0 or self.xshift>0) and not rectagle.semisolid and not rectagle.onewayl:
					self.player.sprite.rect.left = rectagle.rect.right
					player.direction.x = 0
					if rectagle.spr == "W": 
						self.player.sprite.direction.x = 1
						self.player.sprite.xspeed = 4
						self.player.sprite.direction.y = -2
				elif (self.player.sprite.direction.x>0 or self.xshift<0) and not rectagle.semisolid :
					self.player.sprite.rect.right = rectagle.rect.left
					player.direction.x = 0
					if rectagle.spr == "W": 
						self.player.sprite.direction.x = -1
						self.player.sprite.xspeed = 4
						self.player.sprite.direction.y = -2
			elif rectagle.rect.colliderect(self.player.sprite.rect)and rectagle.coin:
				player.paws+=rectagle.value
				if sound:
					pygame.mixer.Sound.play(ding)
				rectagle.kill()
	def collideY(self, pressed_keys):
		player = self.player.sprite
		player.direction.y += player.gravity
		player.rect.y+= player.direction.y
		if player.direction.y < -15 and not player.toggleable["Dash"]:
			player.direction.y = -5
		for rectagle in self.tiles.sprites():
			if rectagle.rect.colliderect(self.player.sprite.rect) and not rectagle.intangible and not rectagle.onewayl:
			#and not rectagle.onewayl:
				if self.player.sprite.direction.y<0 and not rectagle.semisolid :
					if not rectagle.fluid:
						self.player.sprite.rect.top = rectagle.rect.bottom
					player.direction.y = 0
					if rectagle.fluid:
						player.direction.y = 1
				elif self.player.sprite.direction.y>0:
					if not rectagle.fluid:
						if not (rectagle.semisolid and (pressed_keys[K_DOWN] or pressed_keys[K_s])):
							self.player.sprite.rect.bottom = rectagle.rect.top
							player.direction.y = 0
					if rectagle.fluid:
						if pressed_keys[K_DOWN] or pressed_keys[K_s]:
							player.direction.y = 6
						else:
							player.direction.y = 1
					if not rectagle.spr == "M":
						player.toggleable["grounded"] = True
					if rectagle.spr == "M":
						if sound:
							pygame.mixer.Sound.play(jump)
						if rectagle.active:
							self.player.sprite.direction.y = -15
							rectagle.active = False
							rectagle.image = BounceSheet.get_sprite(0, 0, 30, 32)
					
						elif rectagle.active == False:
							rectagle.image = BounceSheet.get_sprite(0, 0, 30, 32)
							self.player.sprite.direction.y = -5
					if player.delay["Dash"] < 1:
						player.delay["Dash"] = 1
					player.delay["Dash"] += 2
	

	def reload(self, pressed_keys):
		if pressed_keys[K_r]:
			self.createlevel()
			
			self.precipitation += 1
		if self.precipitation > 2:
			self.precipitation = 0
	def loadlevel(self, pressed_keys):
		self.tiles.update(self.xshift, self.yshift, self.precipitation)
		self.tiles.draw(self.screen)
		self.player.draw(self.screen)
		self.reload(pressed_keys)
		#KEEP MOVING THE PLAYER IN COLLIDE FUNCTION otherwise the dog jitters and cause collisions to not work properly
		
		self.collideY(pressed_keys)
		self.collideX()
		
		self.movex(pressed_keys)
		self.movey(pressed_keys)


		

	