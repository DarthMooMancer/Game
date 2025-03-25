from include.System.WindowCore import Window
from include.System.EntityCore import entityManager
from include.System.Display import win
from include.Children.Player import Player
from include.Children.Maps import mapManager, test3
import pygame

class Main(Window):
    def __init__(self, id, manager):
        Window.__init__(self, id, manager)
        self.player = Player()

    def initCallback(self):
        mapManager.setMap(test3)
        entityManager.addToGroup(self.player, "Entity")
        mapManager.tileRenderer()  # This will render the tiles based on the active map

    def updateCallback(self):
        win.fill((0, 0, 0))
        entityManager.update()

    def eventHandler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.manager.switchWindow(self.id, 1)

class Settings(Window):
    def __init__(self, id, manager):
        Window.__init__(self, id, manager)

    def eventHandler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                self.manager.switchWindow(self.id, 0)

    def updateCallback(self):
        win.fill((0, 0, 100))
