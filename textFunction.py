import drawTitleScreen
import pygame

WHITE = (255, 255 , 255)
PINK = (251, 198, 207)

def text_click(mousepos, area): 
    if area.collidepoint(mousepos):
        return True
    return False

def draw_text(screen, font, textStack, index):
    drawTitleScreen.drawTitleScreen(screen, 412, 771, pygame.Rect((0,150,500,150)), PINK)
    print(textStack[index])
    text_out = font.render(textStack[index], False, WHITE)
    screen.blit(text_out, (150,150))
