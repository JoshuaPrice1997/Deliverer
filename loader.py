import pandas as panda
import numpy as np
import pygame

#takes the names of files from tiles.txt and returns a data frame of all the textures
def loadTiles():
    tileDat = np.genfromtxt('Textures/tiles.txt',usecols=range(2),dtype=str)
    d = panda.DataFrame()
    for i in range(tileDat.shape[0]):
        d[tileDat[i][0]] = panda.Series(pygame.transform.scale(pygame.image.load('Textures/'+tileDat[i][1]+'.png').convert(),(128,128)))
    return d

#reads map.txt and displays the textures accordingly
def printTiles(map,tiles,screen):
    #ignores the edge tiles
    for i in range(1,map.shape[1]-1):
        for j in range(1,map.shape[0]-1):
            tile = int(map[j][i])

            #mod is a tuple of the tile modifier and the amount of rotations
            mod = (0,0)
            #Currently only prints road tiles
            if tile == 1:
                #Finding the modifiers
                mod = tileChecker(map,tile,i,j)
                
                #indexes the dataframe to return the appropriate texture
                #The id of the required tile is 10*tile (first digit) and
                #added by the modifier
                tileTex = tiles[str(tile*10+mod[0])][0]
                #rotates the tile the amount of times defined by modifier
                tileTex = pygame.transform.rotate(tileTex,mod[1]*90)
                #Printing at matrix coordinates
                #Tile sizes are constant and will not change with window size
                screen.blit(tileTex,(i*128,j*128))
                
            
def tileChecker(map,t,i,j):
    #THE ROTATION DOESN'T MAKE SENSE TO ME EITHER
    #I did make it though, I think I've made a mistake with the directions

    #An array of the adjacent tiles, starting from the bottom, moving clockwise
    checker = np.array([int(map[j][i-1]),int(map[j+1][i]),int(map[j][i+1]),int(map[j-1][i])])
    
    #amount of rotations
    rotor = 0

    #tile modifier, 0 indicates no adjacent tiles which is unlikely
    mod = 1

    #Number of adjacent tiles that are the same as the current tile
    n = sum(checker == t)

    #indexes of checker where the tiles are not the same
    nope = np.where(checker != t)

    #Depending on how many adjacent tiles there are, the road tile needs
    #to be different, mod ensures that the correct tile is printed
    #If the tile is directional, rotor is based on where the nearby tiles 
    #are to ensure the tile is rotated correctly
    if n == 4:
        #5 indicates intersection
        mod = 5
    elif n == 0:
        #indicates lone tile
        mod = 0
    elif n == 3:
        #indicates t-junction
        mod = 4
        #[0][0] should be the only value in nope, and its index +1 works out to be the 
        #amount of times the tile should be rotated
        rotor = nope[0][0]+1
    elif n == 1:
        #indicates end of a road/building
        mod = 1
        #The tile needs to be rotated 3 extra times before it is the same as the index
        rotor = np.where(checker == t)[0][0]+3
    elif n == 2:
        #either a straight or a turn
        if abs(nope[0][0]-nope[0][1])==2:
            #a straight, the if statement is checking if the adjacent tiles
            #are on opposite sides of the current tile
            mod = 3
            #tbh I thought this should be +1 but it isn't
            rotor = nope[0][0]
        else:
            #it is a turn
            mod = 2
            #Checks the first adjacent tile that is not the same, it works out
            #to rotate that many times plus 1 
            rotor = nope[0][0]+1
            if (nope[0][0] == 0) & (nope[0][1] == 3):
                #if the second different adjacent tile is direction 4, the original texture
                #actually points in right direction and does not need to be roated
                rotor = 0
                #This is because there are two cases where the first different adjacent tile
                #is 1, either pointing from 2 to 3 or 3 to 4.
                #This is the case where the road is pointing from 2 to 3
    return (mod,rotor)


