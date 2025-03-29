import pygame
import sys


#our functions
import drawTitleScreen
import textFunction

pygame.init()
exit = False

SCREEN_WIDTH, SCREEN_HEIGHT = 412, 771
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sakura Cafe")
#image = pygame.image.load("Screenshot.png") #put the background here

#textbox area
textArea = pygame.Rect((0,150,500,150))

#colors 
PINK = (251, 198, 207)
screen.fill(PINK) #screen base color
pygame.display.update()

personality1 = 0
personality2 = 0



def game_loop():
    running = True
    drawTitleScreen.drawTitleScreen(screen, SCREEN_WIDTH, SCREEN_HEIGHT, textArea, PINK);

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #check for other clicks
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                textFunction.text_click(event.pos, textArea)

        pygame.display.update()


game_loop()
