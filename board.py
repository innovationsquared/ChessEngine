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
        self.last_move = None
        self.create()
        self.add_pieces()
    
    def move(self, piece, move):
        initial = move.initial
        target = move.target

        self.squares[target.row][target.col].piece = piece
        self.squares[initial.row][initial.col].piece = None # update last position

        piece.moved = True

        # Clear valid moves
        piece.clear_moves()

        # change last move
        self.last_move = move

        

    def valid_move(self, piece, move):
        return move in piece.moves
        
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

        # bishop, queen and rook all go in lines
        def linear_moves(increments):
            for inc in increments:
                row_inc, col_inc = inc
                potential_move_row = row + row_inc
                potential_move_col = col + col_inc

                while True:
                    if Square.in_range(potential_move_row, potential_move_col):
                        initial = Square(row, col)
                        target = Square(potential_move_row, potential_move_col)
                        move = Move(initial, target)
                        
                        # empty square, add move and continue looping
                        if self.squares[potential_move_row][potential_move_col].isempty():
                            piece.add_move(move)

                        # has enemy, add move, break
                        if self.squares[potential_move_row][potential_move_col].has_rival(piece.color):
                            piece.add_move(move)
                            break # break out if there's a piece
                        
                        # ally piece (break)
                        if self.squares[potential_move_row][potential_move_col].has_ally(piece.color):
                            break # break out if there's a piece

                    # increment increments
                    potential_move_row = potential_move_row + row_inc
                    potential_move_col = potential_move_col + col_inc
                        
        
        if piece.name == 'pawn':
            pawn_moves()
        elif piece.name == 'knight':
            knight_moves()
        elif piece.name == 'bishop':
            linear_moves([
                (-1, 1), 
                (-1, -1),
                (1, 1),
                (1, -1)
            ])
        elif piece.name == 'rook':
            linear_moves([
                (1, 0),
                (0, 1),
                (-1, 0),
                (0, -1)
            ])
        elif piece.name == 'queen':
            linear_moves([
                (-1, 1), 
                (-1, -1),
                (1, 1),
                (1, -1),
                (1, 0),
                (0, 1),
                (-1, 0),
                (0, -1)
            ])
        elif piece.name == 'king':
            pass


    def create(self):
        for row in range(8):
            for col in range(8):
                self.squares[row][col] = Square(row, col)

    def add_pieces(self):
        #pawns
        for col in range (8):
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