#GUI component

import pygame
import sys


#our functions
#import drawTitleScreen

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

WHITE = (255, 255 , 255)
screen.fill(PINK) #screen base color
pygame.display.update()

#font
#pygame.font.init()
#font = pygame.font.SysFont('Comic Sans MS', 10)

personality1 = 0
personality2 = 0

#textStack = []
#textStack = talkitalkirumba.stack1(textStack)
#text_index = 0


def drawTitleScreen(screen, width, height, textArea, color) :
    title_screen_art = pygame.image.load("titleScreenArt.jpeg") #put the background here
    title_screen_art = pygame.transform.scale(title_screen_art, (width, height))
    screen.blit(title_screen_art, (0,0))
    pygame.draw.rect(screen, color, textArea)
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 60)
    text_out = font.render("Sakura Cafe", False, WHITE)
    screen.blit(text_out, (36,178))
    pygame.display.update()

running = True

drawTitleScreen(screen, SCREEN_WIDTH, SCREEN_HEIGHT, textArea, PINK)
#textFunction.draw_text(screen, font, textStack, text_index)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #check for other clicks
        #elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #if textFunction.text_click(event.pos, textArea): # if clicked
                 #text_index += 1
                 #textFunction.draw_text(screen, font, textStack, text_index)
    pygame.display.update()