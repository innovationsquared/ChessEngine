import pygame
ROWS = 8
COLS = 8
SQSIZE = 500 // ROWS
def draw_board(SCREEN):
    for i in range(8):
        for j in range(8):
            rect = (j * SQSIZE, i * SQSIZE, SQSIZE, SQSIZE)
            if (i + j) % 2 == 0:
                pygame.draw.rect(SCREEN, 'white', rect) 
            else:
                pygame.draw.rect(SCREEN, (145, 135, 97), rect)

    
