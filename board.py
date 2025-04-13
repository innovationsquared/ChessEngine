import pygame
from square import Square
from piece import *
ROWS = 8
COLS = 8
SQSIZE = 500 // ROWS
class Board:
    def __init__(self):
        self.squares = [[0,0,0,0,0,0,0,0] for col in range(8)] 
        self.create()
        self.add_pieces()
    
    # Calculate all valid moves of a specific piece at a position.
    def calculate_moves(self, piece, row, col):
        
        # Knight moves
        def knight_moves():
            moves = [(row-2,col+1),(),(),(),(),(),(),()]
        
        
        if piece.name == 'pawn':
            pass

        elif piece.name == 'knight':
            pass

        elif piece.name == 'bishop':
            pass

        elif piece.name == 'rook':
            pass

        elif piece.name == 'queen':
            pass

        elif piece.name == 'king':
            pass


    def create(self):
        for row in range(8):
            for col in range(8):
                self.squares[row][col] = Square(row, col)

    def add_pieces(self):
        #pawns
        for col in range (8):
           #black pawns
           self.squares[1][col] = Square(1, col, Pawn('black'))
           #white pawns
           self.squares[6][col] = Square(6, col, Pawn('white'))
        #knights
        self.squares[0][1] = Square(0, 1, Knight('black'))
        self.squares[0][6] = Square(0, 6, Knight('black'))
        self.squares[7][1] = Square(0, 1, Knight('white'))
        self.squares[7][6] = Square(7, 6, Knight('white'))

        #Bishops
        self.squares[0][2] = Square(0, 2, Bishop('black'))
        self.squares[0][5] = Square(0, 5, Bishop('black'))
        self.squares[7][2] = Square(7,2,Bishop('white'))
        self.squares[7][5] = Square(7,5,Bishop('white'))
        #Rook
        self.squares[0][0] = Square(0, 0, Rook('black'))
        self.squares[0][7] = Square(0, 7, Rook('black'))
        self.squares[7][0] = Square(7,0,Rook('white'))
        self.squares[7][7] = Square(7,7,Rook('white'))
        
        #Kingz
        self.squares[0][4] = Square(0,4, King("black"))
        self.squares[7][4] = Square(7,4, King('white'))
        #queenz
        self.squares[0][3] = Square(0,3, Queen('black'))
        self.squares[7][3] = Square(7,3, Queen('white'))


# Pieces and corresponding locations
# white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
#                 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
# white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
#                    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
# black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
#                 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
# black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
#                    (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
# black_images = ['black_rook.png', 'black_knight.png', 'black_bishop.png', 'black_king.png',
#                 'black_queen.png', 'black_bishop.png', 'black_knight.png', 'black_rook.png',
#                 'black_pawn.png', 'black_pawn.png', 'black_pawn.png', 'black_pawn.png',
#                 'black_pawn.png', 'black_pawn.png', 'black_pawn.png', 'black_pawn.png']


