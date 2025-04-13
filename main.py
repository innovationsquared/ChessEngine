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
        self.game = Game()
        self.board = Board()
        self.selector = Selector()
    
    def mainLoop(self):
        screen = self.SCREEN
        game = self.game
        selector = self.selector
        board = self.board

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
                    piece = None
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

                            if board.valid_move(piece, move):
                                print('valid')
                                board.move(piece, move)
                                # show
                                game.draw_board(screen)
                                game.show_pieces(screen)
                            # if not board.squares[new_row][new_col].has_piece():
                            #     img = pygame.image.load(piece.texture)
                            #     img = pygame.transform.scale(img, (500 // 8, 500 // 8))
                            #     img_center = new_col * SQSIZE + SQSIZE // 2, new_row * SQSIZE + SQSIZE // 2
                            #     piece.texture_rect = img.get_rect(center = img_center)
                            #     screen.blit(img, piece.texture_rect)
                        

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