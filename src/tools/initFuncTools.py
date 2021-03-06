import sys
import os
import pygame

from src.settings import *

#
# initFuncTools
#

# For each main, do this
def initForPyInstaller():
    #Code to check if the code is running from a PyInstaller --onefile .exe
    if getattr(sys, 'frozen', False):
         os.chdir(sys._MEIPASS)

def initPygame():
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
    pygame.font.init()

def initScreen():
    screenSize = (SCREEN_WIDTH, SCREEN_HEIGHT)
    return pygame.display.set_mode(screenSize)