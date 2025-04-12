import pygame

def draw_board(SCREEN, WIDTH, HEIGHT):
    for i in range(32):
        col = i % 4  
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(SCREEN, 'white', [600 - (col * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(SCREEN, 'light gray', [700 - (col * 200), row * 100, 100, 100])
    pygame.draw.rect(SCREEN, 'gray', [0, 800, WIDTH, 100])
    pygame.draw.rect(SCREEN, 'gold', [0, 800, WIDTH, 100], 5)
    pygame.draw.rect(SCREEN, 'gold', [800, 0, 200, HEIGHT], 5)
