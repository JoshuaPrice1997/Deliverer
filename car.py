import pygame
import math

class car:
	
	def __init__(self,image,x=100,y=100,direc=0,speed = 1):
		self.x = x
		self.y = y
		self.direc = direc
		self.image = pygame.transform.rotate(image,direc)
		self.speed = speed
		self.center = image.get_rect().center

	def print(self,screen):
		#The image is rotated during the print process as the original image needs to be kept
		#constantly rotating an image distorts it
		image = pygame.transform.rotate(self.image,360-self.direc)

		#Shift is important because as the image is rotated its size increases
		#in order to keep the car centered the shift is kept track of
		shift = image.get_rect().center[0] - self.center[0]
		#The effect of this can be seen on the menu screen

		screen.blit(image,(self.x-shift,self.y-shift))

	def drive(self,key,map):
		#tank controls hooray
		rad = self.direc*(math.pi/180) 
		if key[pygame.K_w]:

			self.x += self.speed * math.sin(rad)
			self.y -= self.speed * math.cos(rad)


		if key[pygame.K_a]:
			self.direc = (self.direc - self.speed) % 360

		if key[pygame.K_d]:
			self.direc = (self.direc + self.speed) % 360

		if key[pygame.K_s]:
			self.x -= self.speed * math.sin(rad)
			self.y += self.speed * math.cos(rad)


