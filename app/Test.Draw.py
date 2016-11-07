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


    surface1 = DiskSurface(50, GREEN, True)
    litsX = [0,100,100,0]
    listY = [0,0,100,100]
    surface2 = PolygonSurface(litsX, listY, RED, True)


    while True:
        screen.fill(WHITE)

        screen.blit(surface1, [150, 150])
        screen.blit(surface2, [200, 200])

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
        pygame.time.Clock().tick(FPS)
