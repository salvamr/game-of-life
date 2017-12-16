'''
Created on Dec 16, 2017

@author: salva
'''

import pygame
import Cellule

class Board:
    def __init__(self, cells, screen):
        self.cells = cells
        self.screen = screen
        
        self.matrix = [0] * self.cells
        for i in range(self.cells):
            self.matrix[i] = [0] * self.cells
            
    def isInBoard(self, x, y):
        return True if x >= 0 and x < self.cells and y >= 0 and y < self.cells else False

    def setStateByPos(self, x, y, valor):
        if self.isInBoard(y,x):
            self.matrix[y][x] = valor

    def drawBoard(self):
        for x in range(self.cells):
            pygame.draw.line(self.screen, (50,50,50), (self.screen.get_size()[0] / self.cells * x,0), (self.screen.get_size()[0] / self.cells * x, self.screen.get_size()[1]), 1)
        for y in range(self.cells):    
            pygame.draw.line(self.screen, (50,50,50), (0, self.screen.get_size()[1] / self.cells * y), (self.screen.get_size()[0], self.screen.get_size()[1] / self.cells * y), 1)

    def drawCellule(self):
        for y in range(self.cells):
            for x in range(self.cells):
                if self.matrix[y][x] == Cellule.State.ALIVE:
                    xi = self.screen.get_size()[0] / self.cells * x
                    yi = self.screen.get_size()[1] / self.cells * y
                    xf = self.screen.get_size()[0] / self.cells
                    yf = self.screen.get_size()[1] / self.cells
                    pygame.draw.rect(self.screen, (0,255,0), (xi, yi, xf, yf))