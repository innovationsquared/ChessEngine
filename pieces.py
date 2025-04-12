import pygame

# Piece class

class Piece():
    def __init__(self, type, color, image):
        self.type = type
        self.color = color
        self.image = pygame.image.load(image).convert_alpha()

    def getStartingPosition(self):
        
