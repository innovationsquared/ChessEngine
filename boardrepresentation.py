import pygame
none = 0
king = 1
pawn = 2
knight = 3
bishop = 4
rook = 5
queen = 6

white = 8
black = 16
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SQSZ = SCREEN_WIDTH // 8
startFEN = "rnbqkbnr/pppppppp/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

color = 0
def loadPosFromFen(fen):
    squares = [0] * 64
    pieceFromSym = {'k': king, 'p': pawn, 'n': knight, 'b': bishop, 'r': rook, 'q': queen}
    fenboard = fen.split(' ', 1)[0]
    file = 0
    rank = 7
    for c in fenboard:
        if c == '/':
            file = 0
            rank -= 1
        else:
            if c.isdigit():
                file += int(c)
            else:
                if c.isupper():
                    color = white
                else: 
                    color = black
                type = pieceFromSym[c.lower()]
                squares[rank * 8 + file] = type | color
                file += 1
    return squares

def loadBoard(screen, arr):
    piece = ""
    for i in range (0,64):
        rank = i // 8
        file = i % 8 
        color = (arr[i] >> 3) & 0x3
        type = arr[i] & 0x7
        if type==none:
            continue
        if color==1:
            piece = switchWhite.get(type, "piece not found")
        else:
            piece = switchBlack.get(type, "piece not found")
        img = pygame.image.load("images/" + piece)
        img.convert()
        rect = img.get_rect()
        screen.blit(img, (file * SQSZ, rank * SQSZ))



switchWhite = {
    1: "white_king.png",
    2: "white_pawn.png",
    3: "white_knight.png",
    4: "white_bishop.png",
    5: "white_rook.png",
    6: "white_queen.png"
}

switchBlack = {
    1: "black_king.png",
    2: "black_pawn.png",
    3: "black_knight.png",
    4: "black_bishop.png",
    5: "black_rook.png",
    6: "black_queen.png"
}