import pygame
import board
import prompt
from boardrepresentation import *
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hakfish")

# Give instructions
print(prompt.getInstructions())

first_turn = True # as soon as first turn occurs set to false
run = True
while run:

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    SCREEN.fill((145, 135, 97))

    board.draw_board(SCREEN)  
    loadBoard(SCREEN, loadPosFromFen(startFEN))
    pygame.display.update()
    #move = prompt.promptForMove()

pygame.quit()

