from src.tools.basicFuncTools import *

#
# Create a simple screen
#
if __name__ == '__main__':
    initForPyInstaller()
    initPygame()
    screen = initScreen()

    titleIcon = pygame.transform.scale(pygame.image.load(os.path.join('../img', 'pig_sample.png')),
                                       (TILE_DIMX, TILE_DIMY))
    pygame.display.set_icon(titleIcon)
    pygame.display.set_caption("Title of the screen")

    print("Create a simple screen")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
