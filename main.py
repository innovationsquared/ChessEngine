import pygame
import board

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame")
clock = pygame.time.Clock()

run = True

while run:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    SCREEN.fill((145, 135, 97))
    #pygame.draw.rect(SCREEN, 'white', pygame.Rect(30,30,60,60))
    board.draw_board(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT)   
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

