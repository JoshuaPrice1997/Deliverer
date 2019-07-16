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
		self.xVel = 0
		self.yVel = 0
		self.speed = 0
		self.reverseEnabled = True

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
		print('direction ' + str(self.direc) + ' xVel: ' + str(self.xVel) + ', yVel: ' + str(self.yVel) + ', reverse: ' + str(self.reverseEnabled))

		if self.speed <0.1:
			self.reverseEnabled = True

		if key[pygame.K_a]:
			self.direc = (self.direc - 1) % 360

		if key[pygame.K_d]:
			self.direc = (self.direc + 1) % 360

		rad = self.direc*(math.pi/180) 

		if key[pygame.K_w] | key[pygame.K_s]:
			if key[pygame.K_w]:
				if self.xVel < 10:
					self.xVel += self.acc * math.sin(rad)
				if self.yVel <10:
					self.yVel -= self.acc * math.cos(rad)
				if self.speed < 10:
					self.speed += self.acc

				if self.speed > 0:
					self.reverseEnabled = False
			if key[pygame.K_s]:
				if self.reverseEnabled:
					if self.xVel > -10:
						self.xVel -= self.acc * math.sin(rad)
					if self.yVel > -10:
						self.yVel += self.acc * math.cos(rad)
					if self.speed > -10:
						self.speed -= self.acc
				else:
					if self.xVel < 0:
						self.xVel += self.acc 
					elif self.xVel > 0:
						self.xVel -= self.acc 

					if self.yVel < 0:
						self.yVel += self.acc
					elif self.yVel > 0:
						self.yVel -= self.acc

					if self.speed > 0:
						self.speed -= self.acc 
					elif self.speed <0:
						self.speed += self.acc 
		else:
			#Friction slows you harder if you are going faster
			if self.xVel < 0:
				self.xVel += self.acc * -self.xVel/10
			elif self.xVel > 0:
				self.xVel -= self.acc * self.xVel/10

			if self.yVel < 0:
				self.yVel += self.acc * -self.yVel/10
			elif self.yVel > 0:
				self.yVel -= self.acc * self.yVel/10

			if self.speed > 0:
				self.speed -= self.acc * self.speed/10
			elif self.speed <0:
				self.speed += self.acc * -self.speed/10

			if abs(self.xVel) < 0.1:
				self.reverseEnabled = True
				self.xVel = 0
			if abs(self.yVel) < 0.1:
				self.reverseEnabled = True
				self.yVel = 0

		
		self.x += self.xVel
		self.y += self.yVel


