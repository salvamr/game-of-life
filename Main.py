'''
Created on Dec 16, 2017

@author: salva
'''

import pygame
import Cellule

from Game import Game
from pygame.locals import *
from Board import Board

def start():
    boardSize = 100
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("GameOfLife")
    game = Game(Board(boardSize, screen))
    pause = True
    leave = False
    while not leave:
        pygame.time.Clock().tick(100)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                leave = True
            if evento.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    pause = not pause
            if evento.type == pygame.MOUSEMOTION or evento.type == pygame.MOUSEBUTTONDOWN:
                x = int(pygame.mouse.get_pos()[0] * boardSize / screen.get_size()[0])
                y = int(pygame.mouse.get_pos()[1] * boardSize / screen.get_size()[1])
                
                #0 left click 2 right click
                if pygame.mouse.get_pressed()[0] == 1:
                    game.board.setStateByPos(x,y, Cellule.State.ALIVE)
                elif pygame.mouse.get_pressed()[2] == 1:
                    game.board.setStateByPos(x,y,Cellule.State.DEAD)

        screen.fill((0,0,0))
        game.board.drawBoard()
        game.board.drawCellule()
        
        if not pause:
            game.update()
        
        pygame.display.flip()


if __name__ == '__main__':
    start()
