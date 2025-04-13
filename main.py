import pygame
import board
import prompt

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hackfish")
#clock = pygame.time.Clock()
pygame.display.set_caption("Cockfish")

# Give instructions
print(prompt.getInstructions())

run = True
while run:

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    SCREEN.fill((145, 135, 97))
    board.draw_board(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT)   
    pygame.display.update()

    board.draw_board(SCREEN, SCREEN_HEIGHT)  

    move = prompt.promptForMove()

    pygame.display.update()

pygame.quit()

