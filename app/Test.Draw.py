from src.tools.basicFuncTools import *
from src.tools.initFuncTools import *

from src.surfaces.simpleSurface import *

#
# Screen with some drawing
#
if __name__ == '__main__':
    initForPyInstaller()
    initPygame()
    screen = initScreen()
    screen.fill(WHITE)

    titleIcon = pygame.transform.scale(pygame.image.load(os.path.join('../img', 'pig_sample.png')),
                                       (TILE_DIMX, TILE_DIMY))
    pygame.display.set_icon(titleIcon)
    pygame.display.set_caption("Screen with some drawing")

    surfaceList = []
    surfaceList.append(diskSurface(50, GREEN, 5))
    listPoint = [[0,0],[100,0],[100,100],[0,100]]
    surfaceList.append(polygonSurface(listPoint, RED, 5))
    listPoint = [[0,0],[100,0],[200,100],[120,80],[-50,100]]
    surfaceList.append(polygonSurface(listPoint, BLUE, 10))
    surfaceList.append(rectSurface([60,100], GREEN, 5))
    listPoint = [[0,0],[100,0],[100,100]]
    surfaceList.append(polygonSurface(listPoint, BLUE, 5))

    positionList = []
    positionList.append([150, 150])
    positionList.append([200, 200])
    positionList.append([200, 400])
    positionList.append([400, 150])
    positionList.append([0, 0])


    while True:
        screen.fill(WHITE)

        iter = 0
        for surface in surfaceList:
            screen.blit(surface, positionList[iter])
            iter += 1

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
        pygame.time.Clock().tick(FPS)
