class Square:
    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece

    def has_piece(self):
        return self.piece != None
    
    def is_empty(self):
        return self.piece == None
    
    # Determine if the square has an ally or rival piece on it
    def has_ally(self, color):
        return self.has_piece() and self.piece_color == color
    
    def has_rival(self, color):
        return self.has_piece() and self.piece.color != color

    # Check for empty squares or enemy pieces
    def check_empty_or_rival(self, color):
        return self.has_piece or self.has_rival
    
    # Check if the positions are in the bounds of the board
    @staticmethod
    def in_range(*args):
        for arg in args:
            if arg < 0 or arg > 7:
                return False
        return True
    

