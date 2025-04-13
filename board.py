import pygame
from square import Square
from piece import *
from move import *

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
        
        # Pawn moves
        def pawn_moves():
            # allowed steps for pawn (2 if pawn has not moved)
            if piece.moved:
                steps = 1 
            else:
                steps = 2
            
            # potential vertical moves
            start = row + piece.dir 
            # move in the direction (-1 or 1) the number of steps
            # add 1 to account for excluded (in range)
            end = row + (piece.dir * (1 + steps))
            for move_row in range(start, end, piece.dir):
                # check to make sure the square is in range and empty
                if Square.in_range(move_row):
                    if self.squares[move_row][col].is_empty():
                        # create initial and target moves
                        initial = Square(move_row, col)
                        target = Square(move_row, col)
                        move = Move(initial, target)
                        piece.add_move(move)
                    # blocked by another piece
                    else:
                        break
                # not in range
                else:
                    break
            
            # diagonal moves
            move_row = row + piece.dir
            move_cols = [col-1,col+1]
            
            for move_col in move_cols:
                # check for in range and has an enemy on the target square
                if Square.in_range(move_row, move_col):
                    if self.squares[move_row][move_col].has_rival(piece.color):
                        initial = Square(move_row, move_col)
                        target = Square(move_row, move_col)
                        move = Move(initial,target)
                        piece.add_move(move)

            

        # Knight moves
        def knight_moves():
            potential_moves = [(row-2,col+1),(row+2,col+1),(col+2,row-1),(row-2,col-1),
                     (row+1,col+2),(row+1,col-2),(row-1,col+2),(row-1,col-2)]

            for potential_move in potential_moves:
                potential_move_row, potential_move_col = potential_move
                if Square.check_range(potential_move_row,potential_move_col):
                    if self.squares[potential_move_row][potential_move_col].is_empty_or_rival(piece.color):
                        
                        initial = Square(row, col) # starting square
                        target = Square(potential_move_row, potential_move_col) # target squares
                        # create a new move for all of the valid moves
                        move = Move(initial, target)
                        piece.add_move(move)

        
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

    def add_pieces(self, color):
        row_pawn, row_other = (6,7) if color == 'white' else (1,0)

        #pawns
        for col in range (8):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))
        
        #knight
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))

        #bishops
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))

        # rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))

        # queen
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))

        #king
        self.squares[row_other][4] = Square(row_other, 4, King(color))
