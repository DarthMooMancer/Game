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

    def initCallback(self):
        chmap.mapManager.setMap(chmap.test1)

    def updateCallback(self):
        dp.win.fill((0, 0, 0))
        print("This is main")
        ent.entityManager.update("Entity")
        ent.entityManager.update("Obstacle")
        
        chmap.mapManager.tileRenderer()  # This will render the tiles based on the active map

    def eventHandler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                chent.player.clearVelocity()
                self.manager.switchWindow(self.id, 1)

        chent.player.eventHandler(event)

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
        print("This is settings")

    def update(self):
        self.render.update()
