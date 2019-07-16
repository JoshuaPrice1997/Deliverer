import pygame
import math

class car:
	
	def __init__(self,image,x=100,y=100,direc=0,acc = 0.1):
		self.x = x
		self.y = y
		self.direc = direc
		self.image = pygame.transform.rotate(image,direc)
		self.center = image.get_rect().center
		self.acc = acc
		self.xSpeed = 0
		self.ySpeed = 0

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
		print('direction ' + str(self.direc) + ' xSpeed: ' + str(self.xSpeed) + ', ySpeed: ' + str(self.ySpeed))
		if key[pygame.K_a]:
			self.direc = (self.direc - 1) % 360

		if key[pygame.K_d]:
			self.direc = (self.direc + 1) % 360

		rad = self.direc*(math.pi/180) 

		if key[pygame.K_w] | key[pygame.K_s]:
			if key[pygame.K_w]:
				if self.xSpeed < 10:
					self.xSpeed += self.acc * math.sin(rad)
				if self.ySpeed <10:
					self.ySpeed -= self.acc * math.cos(rad)
			if key[pygame.K_s]:
				if self.xSpeed > -10:
					self.xSpeed -= self.acc * math.sin(rad)
				if self.ySpeed > -10:
					self.ySpeed += self.acc * math.cos(rad)
		else:
			if self.xSpeed < 0:
				self.xSpeed += self.acc * -self.xSpeed/10
			elif self.xSpeed > 0:
				self.xSpeed -= self.acc * self.xSpeed/10

			if self.ySpeed < 0:
				self.ySpeed += self.acc * -self.ySpeed/10
			elif self.ySpeed > 0:
				self.ySpeed -= self.acc * self.ySpeed/10

			if abs(self.xSpeed) < 0.1:
				self.xSpeed = 0
			if abs(self.ySpeed) < 0.1:
				self.ySpeed = 0

		
		self.x += self.xSpeed
		self.y += self.ySpeed


