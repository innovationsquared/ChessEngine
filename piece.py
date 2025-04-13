import pygame
import move
import os
# Piece class

class Piece():
    def __init__ (self, type, color, value, texture=None, texture_rect=None):
        self.type = type
        self.color = color
        valuesn = 1 if color == 'white' else -1
        self.value = value * valuesn
        self.moves = []
        self.moved = False
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect
    
    def set_texture(self, size=80):
        self.texture = os.path.join(f'images/{self.color}_{self.type}.png')
        

    def add_move(self, move):
        self.moves.append(move)

class Pawn(Piece):
    def __init__(self, color):
        self.dir = -1 if color == 'white' else 1
        super().__init__('pawn', color, 1.0)

class Knight(Piece):
    def __init__(self, color):
        super().__init__('knight', color, 3.0)

class Bishop(Piece):
    def __init__(self, color):
        super().__init__('bishop', color, 3.001)

class Rook(Piece):
    def __init__(self, color):
        super().__init__('rook', color, 5.0)

class Queen(Piece):
    def __init__(self, color):
        super().__init__('queen', color, 9.0)

class King(Piece):
    def __init__(self, color):
        super().__init__('king', color, 1000.0)

# Dictionary for pieces and their positions



#for i in range(len(black_pieces)):
#    piece = Piece(black_pieces[i], 'black', black_locations[i], black_images[i])
