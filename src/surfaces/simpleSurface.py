from src.tools.initFuncTools import *
import math

#
# SimpleSurface
#
class SimpleSurface(pygame.Surface):
    def __init__(self, dimension):
        super().__init__(dimension, pygame.SRCALPHA, 32)
        self.surfaceRatio = 1
        self.baseRatio = 9/10

#
# DiskSurface
#
class DiskSurface(SimpleSurface):
    def __init__(self, radius=1, color=BLACK, border=False):
        super().__init__([2*radius, 2*radius])
        if border:
            self.surfaceRatio = self.baseRatio
            pygame.draw.circle(self, BLACK, [radius, radius], radius)
        pygame.draw.circle(self, color, [radius, radius], math.floor(radius*self.surfaceRatio))

#
# PolygonSurface
#
class PolygonSurface(SimpleSurface):
    def __init__(self, pointListX, pointListY, color=BLACK, border=False):
        super().__init__([max(pointListX)-min(pointListX), max(pointListY)-min(pointListY)])
        dimList = len(pointListX)
        centerX = sum(pointListX)/dimList
        centerY = sum(pointListY)/dimList
        pointList = []
        pointListIn = []
        ratio = 1-self.baseRatio
        for k in range(0, dimList):
            pointList.append([pointListX[k], pointListY[k]])
            if border:
                if centerX > pointListX[k]:
                    ptX = math.floor(pointListX[k]*(1-ratio) + centerX*ratio)
                else:
                    ptX = math.ceil(pointListX[k]*(1-ratio) + centerX*ratio)
                if centerY > pointListY[k]:
                    ptY = math.floor(pointListY[k]*(1-ratio) + centerY*ratio)
                else:
                    ptY = math.ceil(pointListY[k]*(1-ratio) + centerY*ratio)
                pointListIn.append([ptX, ptY])

        if border:
            pygame.draw.polygon(self, BLACK, pointList)
            pygame.draw.polygon(self, color, pointListIn)
        else:
            pygame.draw.polygon(self, color, pointList)
