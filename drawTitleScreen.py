import pygame
WHITE = (255, 255 , 255)

def drawTitleScreen(screen, width, height, textArea, color) :
    title_screen_art = pygame.image.load("titleScreenArt.jpeg") #put the background here
    title_screen_art = pygame.transform.scale(title_screen_art, (width, height))
    screen.blit(title_screen_art, (0,0))
    pygame.draw.rect(screen, color, textArea)
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 50)
    text_out = font.render("Sakura Cafe", False, WHITE)
    screen.blit(text_out, (100,150))
    pygame.display.update()