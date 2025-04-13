import pygame
import board

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400

pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hackfish")
#clock = pygame.time.Clock()

run = True

while run:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    SCREEN.fill((145, 135, 97))
    board.draw_board(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT)   
    pygame.display.update()

pygame.quit()

