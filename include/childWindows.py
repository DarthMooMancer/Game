from include import Window as win
from include import Display as dp
from include import Entity as ent
from include import ChildEntities as chent
import pygame
from include.Settings import *

entityManager = ent.EntityManager(dp.win)
player = chent.Player()
entityManager.addGroup("Entity")
entityManager.addToGroup(player, "Entity")

class Main(win.Window):
    def __init__(self, name, id, manager):
        win.Window.__init__(self, name, id, manager)
        self.render = dp.newGraphicRender(self, 30, self.updateCallback, eventHandler=self.eventHandler)

    def updateCallback(self):
        dp.win.fill((0, 0, 0))
        entityManager.update("Entity")

    def eventHandler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                player.clearVelocity()
                self.manager.switchWindow(self.id, 1)

        player.eventHandler(event)

    def update(self):
        self.render.update()

class Settings(win.Window):
    def __init__(self, name, id, manager):
        win.Window.__init__(self, name, id, manager)
        self.render = dp.newGraphicRender(self, 30, self.updateCallback, eventHandler=self.eventHandler)

    def eventHandler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.manager.switchWindow(self.id, 0)

    def updateCallback(self):
        dp.win.fill((0, 0, 100))

    def update(self):
        self.render.update()
