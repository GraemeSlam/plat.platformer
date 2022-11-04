import pygame
from tiles import *
from player import *
from settings import tilesize
from random import randint
class level:
	def __init__(self, text, screen):
		self.text = text
		self.screen = screen
		self.xshift = 0
		self.yshift = 0
		self.createlevel()
	def createlevel(self):
		self.tiles = pygame.sprite.Group()
		self.player = pygame.sprite.GroupSingle()
		for row_index,row in enumerate(self.text):
			for symbol_index,symbol in enumerate(row):
				if symbol == "0":
					x = symbol_index*tilesize
					y = row_index*tilesize
					Tile = tile((x, y), tilesize, 0)
					self.tiles.add(Tile)
				elif symbol == "1":
					x = symbol_index*tilesize
					y = row_index*tilesize
					Tile = tile((x, y), tilesize, 1)
					self.tiles.add(Tile)
				elif symbol == "2":
					x = symbol_index*tilesize
					y = row_index*tilesize
					Fox = player((x+5, y))
					self.player.add(Fox)
				elif symbol == "3":
					x = symbol_index*tilesize+randint(0,25)
					y = row_index*tilesize+24
					Tile = tile((x, y), tilesize, 3)
					self.tiles.add(Tile)
				elif symbol == "4":
					x = symbol_index*tilesize
					y = row_index*tilesize+8
					Tile = tile((x, y), tilesize, 4)
					self.tiles.add(Tile)
				elif symbol == "5":
					x = symbol_index*tilesize
					y = row_index*tilesize-16
					Tile = tile((x, y), tilesize, 5)
					self.tiles.add(Tile)
	def movex (self):
		player = self.player.sprite
		if player.rect.centerx < 200 and player.direction.x < 0:
			self.xshift = 10
			player.xspeed = 0
		elif player.rect.centerx > 600 and player.direction.x > 0:
			self.xshift = -10
			player.xspeed = 0
		else:
			self.xshift = 0
			player.xspeed = 5
	def movey (self):
		player = self.player.sprite
		if player.rect.centery < 200 and player.direction.y < 0:
			self.yshift = -player.direction.y
			player.yspeed = 0
		elif player.rect.centery > 500 and player.direction.y > 0:
			self.yshift = -player.direction.y
			player.yspeed = 0
		else:
			self.yshift = 0
			player.yspeed = 5
	def collide(self):
		blockcollide = pygame.sprite.groupcollide(self.tiles, self.player,False, False)
		
		if blockcollide:
			for rectagle in self.tiles.sprites():
				if rectagle.rect.colliderect(self.player.sprite.rect):
					if self.player.sprite.direction.y<0:
						self.player.sprite.rect.top = rectagle.rect.bottom
						
					elif self.player.sprite.direction.y>0:
						self.player.sprite.rect.bottom = rectagle.rect.top
						if rectagle.spr == 4:
							
							if rectagle.active:
								self.player.sprite.direction.y = -15
								rectagle.active = False
								rectagle.image = BounceSheet.get_sprite(0, 0, 30, 32)


							elif rectagle.active == False:
								rectagle.image = BounceSheet.get_sprite(0, 0, 30, 32)
								self.player.sprite.direction.y = -5

						else:
							self.player.sprite.direction.y = 0


			for rectagle in self.tiles.sprites():
				if rectagle.rect.colliderect(self.player.sprite.rect):
					if self.player.sprite.direction.x<0:
						self.player.sprite.rect.left = rectagle.rect.right
						if rectagle.spr == 5: 
							self.player.sprite.direction.y = -5
							self.player.sprite.direction.x = -5
					elif self.player.sprite.direction.x>0:
						self.player.sprite.rect.right = rectagle.rect.left
						if rectagle.spr == 5: 
							self.player.sprite.direction.y = 5
							self.player.sprite.direction.x = 5
			
	def loadlevel(self):
		self.collide()
		self.tiles.update(self.xshift, self.yshift)
		self.tiles.draw(self.screen)
		self.player.draw(self.screen)
		self.movex()
		self.movey()
		

	