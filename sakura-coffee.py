import pygame
import sys


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
screen.fill(PINK) #screen base color
pygame.display.update()

personality1 = 0
personality2 = 0



def game_loop():
    running = True
    drawTitleScreen.drawTitleScreen();

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #check for other clicks

        pygame.display.update()


game_loop()
