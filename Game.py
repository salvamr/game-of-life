'''
Created on Dec 10, 2017

@author: salva
'''
import copy
import Cellule

class Game:
    def __init__(self, board):
        self.board = board

    def update(self):
        tempBoard = copy.deepcopy(self.board.matrix)
        
        for y in range(0, self.board.cells):
            for x in range(0, self.board.cells):
                neighbors = 0
                
                try:
                    if self.board.matrix[x][y - 1] == Cellule.State.ALIVE:
                        neighbors += 1
                    if self.board.matrix[x][y + 1] == Cellule.State.ALIVE:
                        neighbors += 1
                    if self.board.matrix[x - 1][y] == Cellule.State.ALIVE:
                        neighbors += 1
                    if self.board.matrix[x + 1][y] == Cellule.State.ALIVE:
                        neighbors += 1
                    if self.board.matrix[x + 1][y - 1] == Cellule.State.ALIVE:
                        neighbors += 1
                    if self.board.matrix[x - 1][y - 1] == Cellule.State.ALIVE:
                        neighbors += 1
                    if self.board.matrix[x + 1][y + 1] == Cellule.State.ALIVE:
                        neighbors += 1
                    if self.board.matrix[x - 1][y + 1] == Cellule.State.ALIVE:
                        neighbors += 1
                except:
                    pass
                
                if neighbors == 3:
                    tempBoard[x][y] = Cellule.State.ALIVE
                elif neighbors > 3 or neighbors < 2:
                    tempBoard[x][y] = Cellule.State.DEAD
    
        self.board.matrix = tempBoard;