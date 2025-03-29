import pygame
import random
import math


#our functions
import drawTitleScreen


pygame.init()
exit = False

SCREEN_WIDTH, SCREEN_HEIGHT = 320, 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sakura Cafe")
#image = pygame.image.load("Screenshot.png") #put the background here

#colors 
PINK = (251, 198, 207)
screen.fill(PINK)

personality1 = 0
personality2 = 0


while not exit:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
        else:
            #run thorugh main program


        pygame.display.update()