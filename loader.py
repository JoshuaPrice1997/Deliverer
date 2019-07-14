import pandas as panda
import numpy as np
import pygame

def loadTiles():
    tileDat = np.genfromtxt('Textures/tiles.txt',usecols=range(2),dtype=str)
    d = panda.DataFrame()
    for i in range(tileDat.shape[0]):
        d[tileDat[i][0]] = panda.Series(pygame.transform.scale(pygame.image.load('Textures/'+tileDat[i][1]+'.png').convert(),(128,128)))
    return d

def printTiles(map,tiles,screen):
    for i in range(map.shape[0]-2):
        for j in range(map.shape[1]-2):
            tile = int(map[j+1][i+1])
            print((i,j))
            print(tile)
            mod = (0,0)
            if tile == 1:
                mod = tileChecker(map,tile,i+1,j+1)
                print(mod)
                tileTex = tiles[str(tile*10+mod[0])][0]
                tileTex = pygame.transform.rotate(tileTex,mod[1]*90)
                screen.blit(tileTex,(i*128,j*128))
                
            
def tileChecker(map,t,i,j):
    #THE ROTATION DOESN'T MAKE SENSE TO ME EITHER
    #I did make it though

    
    checker = np.array([int(map[j][i-1]),int(map[j+1][i]),int(map[j][i+1]),int(map[j-1][i])])
    rotor = 0
    mod = 1
    n = sum(checker == t)
    nope = np.where(checker != t)

    if n == 4:
        mod = 5
    elif n == 0:
        mod = 0
    elif n == 3:
        mod = 4
        rotor = nope[0][0]
    elif n == 1:
        mod = 1
        rotor = np.where(checker == t)[0][0]+3
    elif n == 2:
        if abs(nope[0][0]-nope[0][1])==2:
            mod = 3
            rotor = nope[0][0]
        else:
            mod = 2
            rotor = nope[0][0]+1
            if nope[0][1] == 4:
                rotor = 0
    return (mod,rotor)


