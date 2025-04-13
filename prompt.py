# Get user input for moves
def getInstructions():
    instructions = "You play as white.\n" \
    "Please enter all moves in algebraic notation." \
    "\n(Ex. e4, Nf3, etc.)"     
    return instructions

def promptForMove():    
    move = input("Enter your move: ")
    return move

