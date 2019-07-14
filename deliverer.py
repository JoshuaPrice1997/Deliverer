import pygame
import numpy as np
import pandas as panda
from loader import *

def main():

    #initialize the pygame module
    pygame.init()
    pygame.font.init()
    if not pygame.font: print('Warning, fonts disabled')
    #Logo
    logo = pygame.image.load("Textures/logo.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("")
     
    #Default window size 720p
    screen = pygame.display.set_mode((1280,720),pygame.RESIZABLE)
    #Keeps track of window size
    MAXX = 1280
    MAXY = 720
    #default player position
    x = y = 100
    #keeps track of game state
    state = 0
    running = True
    #importing assets
    tiles = loadTiles()
    #text = loadText()
    player = pygame.image.load('Textures/car.png').convert()
    mapo = np.loadtxt('map.txt',usecols=range(7))

    while running:
        #loading current key presses
        key = pygame.key.get_pressed()

        #Checking for certain events
        for event in pygame.event.get():
            #quit game
            if event.type == pygame.QUIT:
                running = False
            #resize window
            if event.type == pygame.VIDEORESIZE:
                #changing parameters
                surface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
                #Updating parameters
                MAXX = event.w
                MAXY = event.h
        
        if state == 0:
            #---------------------#
            #Menu state
            #---------------------#

            fontSize = int(MAXY/10)
            if pygame.font:
            	#There must be a more efficient way of achieving this
            	fonto = pygame.font.Font("\WINDOWS\Fonts\VLADIMIR.TTF",fontSize)
            	title = fonto.render("It's Pizza Time",1,(255,255,255))
            	td = fonto.size("It's Pizza Time")
            	fonto = pygame.font.Font("\WINDOWS\Fonts\VLADIMIR.TTF",int(fontSize/2))
            	enter = fonto.render("Press Enter",1,(255,255,255))
            	ed = fonto.size("Press Enter")
            	#Literally just two sentences
            	screen.blit(title,(MAXX/2-td[0]/2,MAXY/2-td[1]/2))
            	screen.blit(enter,(MAXX/2+ed[0]/2,MAXY/2+td[1]/2))
            #change to game state
            if key[pygame.K_RETURN]:
            	state += 1
            	screen.fill((0,0,0))


        if state == 1:
            #---------------------#
            #Game State
            #---------------------#
            printTiles(mapo,tiles,screen)
            screen.blit(player,(x,y))
            #basic movement
            if key[pygame.K_w]:y -= 10
            if key[pygame.K_a]:x -= 10
            if key[pygame.K_d]:x += 10
            if key[pygame.K_s]:y += 10

        #Quit game
        if key[pygame.K_ESCAPE]:sys.exit

        #Input Lag
        pygame.time.delay(10)

        #Animate
        pygame.display.update()


if __name__=="__main__":
    # call the main function
    main()