import pygame
import moves
import os
# Piece class

class Piece():
    def __init__ (self, type, color, value, texture, texture_rect):
        self.type = type
        self.color = color
        valuesn = 1 if color == 'white' else -1
        self.value = value * valuesn
        self.texture = texture()
        self.set_texture()
        self.texture_rect = texture_rect
    
    def set_texture(self, size=80):
        self.texture = os.path.join('images/' + self.color + '_' + self.type)


# Pieces and corresponding locations
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
black_images = ['black_rook.png', 'black_knight.png', 'black_bishop.png', 'black_king.png',
                'black_queen.png', 'black_bishop.png', 'black_knight.png', 'black_rook.png',
                'black_pawn.png', 'black_pawn.png', 'black_pawn.png', 'black_pawn.png',
                'black_pawn.png', 'black_pawn.png', 'black_pawn.png', 'black_pawn.png']

# Dictionary for pieces and their positions



for i in range(len(black_pieces)):
    piece = Piece(black_pieces[i], 'black', black_locations[i], black_images[i])
