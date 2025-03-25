import sys
import pygame
from include.System.Settings import HEIGHT, WIDTH, FPS

def init():
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()

    win = pygame.display.set_mode((WIDTH, HEIGHT), vsync=1)
    pygame.display.set_caption("Game")
    clock = pygame.time.Clock()
    return win, clock

win, clock = init()

class newGraphicRender:
    def __init__(self, window, updateCallback, initCallback=None, eventHandler=None):
        self.updateCallback = updateCallback
        self.initCallback = initCallback 
        self.eventHandler = eventHandler
        self.window = window

    def update(self):
        if self.initCallback:
            self.initCallback()

        while self.window.status:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if self.eventHandler:
                    self.eventHandler(event)

            self.updateCallback()

            pygame.display.update()
