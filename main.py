import pygame
import prompt
from game import Game 
from selector import Selector
from const import *
from board import Board

class Main:
    def __init__(self):
        pygame.init()
        self.SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Hakfish")
        self.game = Game()
        self.board = Board()
        self.selector = Selector()
    
    def mainLoop(self):
        screen = self.SCREEN
        game = self.game
        selector = self.selector
        board = self.board
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
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        selector.update_pos(event.pos)
                        row_selected = selector.mouseY // SQSIZE
                        col_selected = selector.mouseX // SQSIZE
                        #print(row_selected)
                        #print(col_selected)
                        if board.squares[row_selected][col_selected] 
                            if board.squares[row_selected][col_selected]

                elif event.type == pygame.MOUSEBUTTONUP:
                    pass
                elif event.type == pygame.MOUSEMOTION:
                    pass

            #loadBoard(SCREEN, loadPosFromFen(startFEN))
            pygame.display.update()
            #move = prompt.promptForMove()

        pygame.quit()

main = Main()
main.mainLoop()