# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

BACKGROUND_COLOR = (255,255,255)


#Main font
FONT_NAME = 'arial'

FPS = 60

#DIMENSION
# http://gamedevelopment.tutsplus.com/articles/quick-tip-what-is-the-best-screen-resolution-for-your-game--gamedev-14723
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Dimension tile base for icon
TILE_DIMX = 32
TILE_DIMY = 32


# If you add a Tag for debugging, you MUST set it here at 0 for everyone
# You can turn your tag on in your own settings_local.py for personal use

TAG_DEBUG_BP = 0

# Load settings_local.py if exist
try:
    from src.settings_local import *
except ImportError:
    pass


