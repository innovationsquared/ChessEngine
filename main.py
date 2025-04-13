import pygame
import prompt
from boardrepresentation import *
from game import Game 
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
class Main:
    def __init__(self):
        pygame.init()
        self.SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Hakfish")
        self.game = Game()
    
    def mainLoop(self):
        screen = self.SCREEN
        game = self.game
        # Give instructions
        print(prompt.getInstructions())

        #first_turn = True # as soon as first turn occurs set to false
        run = True
        while run:
            screen.fill((145, 135, 97))
            game.draw_board(screen)  
            game.show_pieces(screen)
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            

            #loadBoard(SCREEN, loadPosFromFen(startFEN))
            pygame.display.update()
            #move = prompt.promptForMove()

        pygame.quit()

main = Main()
main.mainLoop()