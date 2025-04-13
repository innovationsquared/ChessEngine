import pygame
from board import Board
SQSIZE = 500 // 8
class Game:
    def __init__(self):
        self.board = Board()

    def draw_board(self, surface):
        for i in range(8):
            for j in range(8):
                rect = (j * SQSIZE, i * SQSIZE, SQSIZE, SQSIZE)
                if (i + j) % 2 == 0:
                    pygame.draw.rect(surface, (242, 231, 186), rect) 
                else:
                    pygame.draw.rect(surface, (145, 135, 97), rect)

    def show_pieces(self, surface):
        for row in range(8):
            for col in range(8):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    img = pygame.image.load(piece.texture)
                    img = pygame.transform.scale(img, (500 // 8 * 0.85, 500 // 8 * 0.85))
                    img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                    piece.texture_rect = img.get_rect(center = img_center)
                    surface.blit(img, piece.texture_rect)