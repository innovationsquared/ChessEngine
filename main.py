import pygame
from square import *
from game import Game 
from selector import Selector
from const import *
from board import Board
from move import *

class Main:
    def __init__(self):
        pygame.init()
        self.SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Hakfish")
        self.board = Board()
        self.game = Game(self.board)
        self.selector = Selector()
    
    def mainLoop(self):
        screen = self.SCREEN
        game = self.game
        selector = self.selector
        board = self.board
        new_col = 0
        new_row = 0
        initial_col = 0
        initial_row = 0
        piece = None            

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
                    #left click
                    if event.button == 1:
                        selector.update_pos(event.pos)
                        row_selected = selector.mouseY // SQSIZE
                        col_selected = selector.mouseX // SQSIZE
                        #print(row_selected)
                        #print(col_selected)
                        if board.squares[row_selected][col_selected].has_piece():
                          piece = board.squares[row_selected][col_selected].piece
                          initial_row = row_selected
                          initial_col = col_selected
                          print('selected piece')
                    #right click
                    elif event.button == 3:
                        if piece != None:
                            selector.update_pos(event.pos)
                            new_row = selector.mouseY // SQSIZE
                            new_col = selector.mouseX // SQSIZE
                            # create possible move
                            initial = Square(initial_row, initial_col)
                            target = Square(new_row, new_col)
                            move = Move(initial, target)

                            print('working here')
                            board.move(piece, move)
                            # show
                            game.draw_board(screen)
                            game.show_pieces(screen)
            
            pygame.display.update()

        pygame.quit()

main = Main()
main.mainLoop()