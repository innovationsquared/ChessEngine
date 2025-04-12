import pygame
import board

SCREEN_WIDTH = 940
SCREEN_HEIGHT =  540

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame")
clock = pygame.time.Clock()

run = True
while run:

    board.draw_board(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    clock.tick(60)

pygame.quit()

