from os import path

TILESIZE = 32
WIDTH, HEIGHT = 30 * TILESIZE, 21 * TILESIZE # Cols and Rows
FPS = 45

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

gameDir = path.dirname(__file__)

# Game Directory
assetsDir = path.join(gameDir, "assets")
settingsPath = path.join(gameDir, "data/settings.json")

# Assets Directory
imageDir = path.join(assetsDir, "images")
particlePath = path.join(assetsDir, "particles")
soundsPath = path.join(assetsDir, "sounds")
fontDir = path.join(assetsDir, "fonts")

# Image Directory
btnDir = path.join(imageDir, "buttons")
itemDir = path.join(imageDir, "items")
roomDir = path.join(imageDir, "Room")
