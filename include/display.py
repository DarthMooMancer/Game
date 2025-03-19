import pygame
from include.Settings import WIDTH, HEIGHT
import sys

def init():
    pygame.init()
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.mixer.init()
    pygame.font.init()

    win = pygame.display.set_mode((WIDTH, HEIGHT), vsync=1)
    pygame.display.set_caption("Gloombound")
    clock = pygame.time.Clock()
    return win, clock

win, clock = init()

class newGraphicRender:
    def __init__(self, window, fps, updateCallback, initCallback=None, eventHandler=None):
        self.fps = fps
        self.updateCallback = updateCallback
        self.initCallback= initCallback 
        self.eventHandler = eventHandler
        self.window = window

    def update(self):
        if self.initCallback:
            self.initCallback()

        while self.window.enabled:
            clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if self.eventHandler:
                    self.eventHandler(event)

            self.updateCallback()

            pygame.display.update()
