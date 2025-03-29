import pygame

def drawTitleScreen(screen, width, height) :
    title_screen_art = pygame.image.load("titleScreenArt.jpeg") #put the background here
    title_screen_art = pygame.transform.scale(title_screen_art, (width, height))
    screen.blit(title_screen_art, (0,0))
    pygame.display.update()