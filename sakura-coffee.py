import pygame
import random
import math


pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 320, 480

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sakura Cafe")
#image = pygame.image.load("Screenshot.png") #put the background here

exit = False

while not exit:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True

        pygame.display.update()