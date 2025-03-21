from include.system import WindowCore as win
from include.system import Display as dp
from include.system import EntityCore as ent
from include import childEntities as chent
from include import childMaps as chmap
import pygame
from include.system.Settings import *

class Main(win.Window):
    def __init__(self, id, manager):
        win.Window.__init__(self, id, manager)
        self.render = dp.newGraphicRender(self, 30, self.updateCallback, self.initCallback, self.eventHandler)
        self.player = chent.Player()

    def initCallback(self):
        chmap.mapManager.setMap(chmap.test1)
        ent.entityManager.addToGroup(self.player, "Entity")

    def updateCallback(self):
        dp.win.fill((0, 0, 0))
        ent.entityManager.update("Entity")
        ent.entityManager.update("Obstacles")

        # for x in range(0, WIDTH, TILESIZE):
        #     for y in range(0, HEIGHT, TILESIZE):
        #         rect = pygame.Rect(x, y, TILESIZE, TILESIZE)
        #         pygame.draw.rect(dp.win, BLUE, rect, 1)

        chmap.mapManager.tileRenderer()  # This will render the tiles based on the active map

    def eventHandler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                self.player.clearVelocity()
                self.manager.switchWindow(self.id, 1)

        self.player.eventHandler(event)

    def update(self):
        self.render.update()

class Settings(win.Window):
    def __init__(self, id, manager):
        win.Window.__init__(self, id, manager)
        self.render = dp.newGraphicRender(self, 30, self.updateCallback, eventHandler=self.eventHandler)

    def eventHandler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.manager.switchWindow(self.id, 0)

    def updateCallback(self):
        dp.win.fill((0, 0, 100))

    def update(self):
        self.render.update()
