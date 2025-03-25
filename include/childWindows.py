from include.System.Settings import *
from include.System import WindowCore as win
from include.System import EntityCore as ent
from include.System import Display as dp
from include import childEntities as chent
from include import childMaps as chmap
import pygame

class Main(win.Window):
    def __init__(self, id, manager):
        win.Window.__init__(self, id, manager)
        self.player = chent.Player()

    def initCallback(self):
        chmap.mapManager.setMap(chmap.test3)
        ent.entityManager.addToGroup(self.player, "Camera")
        chmap.mapManager.tileRenderer()  # This will render the tiles based on the active map

    def updateCallback(self):
        dp.win.fill((0, 0, 0))
        ent.entityManager.update()

    def eventHandler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.manager.switchWindow(self.id, 1)

class Settings(win.Window):
    def __init__(self, id, manager):
        win.Window.__init__(self, id, manager)

    def eventHandler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                self.manager.switchWindow(self.id, 0)

    def updateCallback(self):
        dp.win.fill((0, 0, 100))
