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
                        initial_row = selector.mouseY // SQSIZE
                        initial_col = selector.mouseX // SQSIZE
                        #print(initial_row)
                        #print(initial_col)
                        if board.squares[initial_row][initial_col].has_piece():
                          selected_piece = board.squares[initial_row][initial_col].piece

                          board.calculate_moves(selected_piece, initial_row, initial_col)
                          print(f'selected {selected_piece.type}')
                    #right click
                    elif event.button == 3:
                    
                        selector.update_pos(event.pos)
                        new_row = selector.mouseY // SQSIZE
                        new_col = selector.mouseX // SQSIZE
                        # create possible move
                        initial = Square(initial_row, initial_col)
                        target = Square(new_row, new_col)
                        print(initial)
                        print(target)
                        user_move = Move(initial, target)
                        if board.valid_move(selected_piece, user_move):
                            print('working here')
                            board.move(selected_piece, user_move)
                            # show
                            game.draw_board(screen)
                            game.show_pieces(screen)
                        
                        #     print('cant move here ')
                        #     break 
                        # if not board.squares[new_row][new_col].has_piece():
                            #     img = pygame.image.load(piece.texture)
                            #     img = pygame.transform.scale(img, (500 // 8, 500 // 8))
                            #     img_center = new_col * SQSIZE + SQSIZE // 2, new_row * SQSIZE + SQSIZE // 2
                            #     piece.texture_rect = img.get_rect(center = img_center)
                            #     screen.blit(img, piece.texture_rect)
            #loadBoard(SCREEN, loadPosFromFen(startFEN))
            pygame.display.update()

        pygame.quit()

main = Main()
main.mainLoop()