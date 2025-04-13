import pygame

class Selector:
    
    def __init__(self):
        self.mouseX = 0
        self.mouseY = 0
        self.piece = None

    def update_pos(self, pos):
        self.mouseX, self.mouseY = pos
        