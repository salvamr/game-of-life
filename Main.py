'''
Created on Dec 10, 2017

@author: salva
'''

import pygame
import Cellule
import random

from pathlib import Path
from configparser import ConfigParser
from Game import Game
from pygame.locals import *
from Board import Board
from cgi import log

def start():
    if (Path('config.ini').exists()):
        
        config = ConfigParser()
        config.read('config.ini')
    
        boardSize = config.getint('INIT', 'boardSize')
        screenX = config.getint('INIT', 'screenX')
        screenY = config.getint('INIT', 'screenY')
        randomInitialState = config.getboolean('INIT', 'randomInitialState')
        restoreSavedBoard = config.getboolean('INIT', 'restoreSavedBoard')
        
        ticks = config.getint('RUNTIME', 'ticks')
        
        pause_icon = pygame.image.load("icons/pause.png")
        play_icon = pygame.image.load("icons/play.png")
        fast_forward_icon = pygame.image.load("icons/fast_forward.png")
        
        screen = pygame.display.set_mode((screenX,screenY))
        pygame.display.set_caption("Game of Life: BETA")
        game = Game(Board(boardSize, screen))
        
        if randomInitialState:
            for x in range(boardSize):
                for y in range(boardSize):
                    game.board.matrix[x][y] = random.randint(0, 1)
                
        if restoreSavedBoard and not randomInitialState:
            game.board.restoreSavedBoard()
            
        pause = True
        configLoaded = False
        fastForwarding = False
        tickCapture = 0
        boardSaved = False
        
        while True:
            pygame.time.Clock().tick(ticks)

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    #Quit
                    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                        quit()
                    #Pause game
                    if pygame.key.get_pressed()[pygame.K_SPACE]:
                        pause = not pause
                        fastForwarding = False if fastForwarding else False
                    #Clean board
                    if pygame.key.get_pressed()[pygame.K_c]:
                        game = Game(Board(boardSize, screen))
                    #Reload 'runtime' config
                    if pygame.key.get_pressed()[pygame.K_r]:
                        config.read('config.ini')
                        ticks = config.getint('RUNTIME', 'ticks')
                        configLoaded = True
                        tickCapture = pygame.time.get_ticks()
                    #Snapshot current board and save it    
                    if pygame.key.get_pressed()[pygame.K_s]:
                        game.board.saveCurrentBoard()
                        boardSaved = True
                        tickCapture = pygame.time.get_ticks()
                    #Manually update the game
                    if pygame.key.get_pressed()[K_RIGHT] and pause:
                        game.update()
                        fastForwarding = True
                #Add or remove cellules
                if evento.type == pygame.MOUSEMOTION or evento.type == pygame.MOUSEBUTTONDOWN:
                    x = int(pygame.mouse.get_pos()[0] * boardSize / screen.get_size()[0])
                    y = int(pygame.mouse.get_pos()[1] * boardSize / screen.get_size()[1])
                    
                    #0 left click 2 right click
                    if pygame.mouse.get_pressed()[0] == 1:
                        game.board.setStateByPos(x,y, Cellule.State.ALIVE)
                    elif pygame.mouse.get_pressed()[2] == 1:
                        game.board.setStateByPos(x,y,Cellule.State.DEAD)
            
            screen.fill((0,0,0))
            
            #Draw board and cellules
            game.board.drawBoard()
            game.board.drawCellule()
            
            #Draw basic info
            game.board.drawAliveCells()
            game.board.drawText('TICKS: ' + ticks.__str__(), 0, 20)
            
            #Draw controls
            game.board.drawText('SPACE: Run / Stop', 0, 60)
            game.board.drawText('C: Clean board', 0, 80)
            game.board.drawText('R: Reload config', 0, 100)
            game.board.drawText('S: Save current board', 0, 120)
            game.board.drawText('Right arrow: update manually', 0, 140)
            game.board.drawText('Left click: add cellule', 0, 160)
            game.board.drawText('Right click: delete cellule', 0, 180)

            if configLoaded:
                game.board.drawText('Config loaded!', screen.get_size()[0] / 2, screen.get_size()[1] / 2)
                #Wait 1 second from tickCapture
                if pygame.time.get_ticks() - tickCapture > 1000:
                    configLoaded = False 
            
            if boardSaved:
                game.board.drawText('Board saved!', screen.get_size()[0] / 2, screen.get_size()[1] / 2)
                #Wait 1 second from tickCapture
                if pygame.time.get_ticks() - tickCapture > 1000:
                    boardSaved = False         
                
            if not pause:
                game.update()
                screen.blit(play_icon, (screen.get_size()[0] / 2, 0))
            else:
                if fastForwarding:
                    screen.blit(fast_forward_icon, (screen.get_size()[0] / 2, 0))
                else:
                    screen.blit(pause_icon, (screen.get_size()[0] / 2, 0))
                 
            pygame.display.flip()
    
    else:
        print('Config file needed')

if __name__ == '__main__':
    start()
