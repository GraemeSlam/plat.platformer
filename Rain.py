from settings import path
import random
class rain:
def __init__(self):
	self.speed = random.randint(7, 12)
	self.image = pygame.image.load(path"RainDrop.png")
	self.rect = self.image.get_rect(
		center=(
				random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
				random.randint(0, SCREEN_HEIGHT),
			)
	)	
	
	def update(self):	
	self.rect.move_ip(0, self.speed)
	if self.rect.right < 0:	
		self.kill()