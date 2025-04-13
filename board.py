import pygame

def draw_board(SCREEN, HEIGHT):
    for i in range(32):
        col = i % 4  
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(SCREEN, (242, 231, 194), [300 - (col * 100), row * 50, 50, 50])
        else:
            pygame.draw.rect(SCREEN, (242, 231, 194), [350 - (col * 100), row * 50, 50, 50])

    pygame.draw.rect(SCREEN, (222, 210, 172), [400, 0, 100, HEIGHT], 5)

    
