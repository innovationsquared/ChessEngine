import pygame
from board import Board
from const import *

class Game:
    def __init__(self,board):
        self.board = board

    def draw_board(self, surface):
        for i in range(8):
            for j in range(8):
                rect = (j * SQSIZE, i * SQSIZE, SQSIZE, SQSIZE)
                if (i + j) % 2 == 0:
                    pygame.draw.rect(surface, (200, 190, 145), rect) 
                else:
                    pygame.draw.rect(surface, (145, 135, 97), rect)
        # added border
        pygame.draw.rect(surface, (145, 135, 97), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 5)


    def show_pieces(self, surface):
        for row in range(8):
            for col in range(8):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    img = pygame.image.load(piece.texture)
                    img = pygame.transform.scale(img, (500 // 8, 500 // 8))
                    img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                    piece.texture_rect = img.get_rect(center = img_center)
                    surface.blit(img, piece.texture_rect)