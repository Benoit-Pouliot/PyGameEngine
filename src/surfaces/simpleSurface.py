import pygame
import numpy

from src.settings import *
from src.tools.timerTools import *

#
# SimpleSurface
#
class SimpleSurface(pygame.Surface):
    def __init__(self, dimension):
        super().__init__(dimension, pygame.SRCALPHA, 32)

#
# rectSurface
#
def rectSurface(dimension, color=BLACK, border=0):
    if border >= 1:
        surface = pygame.Surface(dimension)
        surface.fill(BLACK)
        surface2 = pygame.Surface([dimension[0]-2*border, dimension[1]-2*border])
        surface2.fill(color)
        surface.blit(surface2, [border,border])
    else:
        surface = pygame.Surface(dimension)
        surface.fill(color)
    return surface

#
# diskSurface
#
def diskSurface(radius=1, color=BLACK, border=0):
    surface = SimpleSurface([2*radius, 2*radius])
    if border >= 1:
        pygame.draw.circle(surface, BLACK, [radius, radius], radius)
    pygame.draw.circle(surface, color, [radius, radius], radius-border)
    return surface

#
# polygonSurface
#
# http://gamedev.stackexchange.com/questions/118471/fast-flood-fill-in-pygame
# http://pygame.org/docs/tut/surfarray/SurfarrayIntro.html
# http://www.pygame.org/docs/ref/surfarray.html
# http://stackoverflow.com/questions/17506098/setting-alpha-using-pixels-alpha-in-pygame
#
def polygonSurface(pointsList, color=BLACK, border=0):
    pointListX = [item[0] for item in pointsList]
    pointListY = [item[1] for item in pointsList]
    pointListX = [item-min(pointListX) for item in pointListX]
    pointListY = [item-min(pointListY) for item in pointListY]
    dimX = max(pointListX)
    dimY = max(pointListY)

    pointList = []
    for k in range(0, len(pointsList)):
        pointList.append([pointListX[k], pointListY[k]])

    surface = SimpleSurface([dimX, dimY])
    pygame.draw.polygon(surface, color, pointList)

    # black : [0,0,0]
    # white : [255,255,255]
    # Alpha transp : 0
    if border >= 1:
        surfaceOut = SimpleSurface([dimX, dimY])
        pygame.draw.polygon(surfaceOut, BLACK, pointList)

        refAlpha = pygame.surfarray.pixels_alpha(surface)
        for iter in range(0,border-1):
            refAlphaCopy = numpy.copy(refAlpha)
            refAlphaCopy //= 255
            refAlpha[1:,:]  *= refAlphaCopy[:-1,:]
            refAlpha[:-1,:] *= refAlphaCopy[1:,:]
            refAlpha[:,1:]  *= refAlphaCopy[:,:-1]
            refAlpha[:,:-1] *= refAlphaCopy[:,1:]
            del refAlphaCopy

        refAlpha[0:(border-1),:] = 0
        refAlpha[-1:-border:-1,:] = 0
        refAlpha[:,0:(border-1)] = 0
        refAlpha[:,-1:-border:-1] = 0
        del refAlpha

        surfaceOut.blit(surface, [0,0])
        return surfaceOut
    return surface
#