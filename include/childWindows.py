from include import Window as win
from include import Display as dp
from include import Entity as ent
import pygame
from include.Settings import *

entityManager = ent.EntityManager(dp.win)
player = ent.Entity(16, BLUE, (100, 100))
entityManager.addGroup("Entity", pygame.sprite.Group)
entityManager.addToGroup(player, "Entity")

class Main(win.Window):
    def __init__(self, name, status, id, manager):
        win.Window.__init__(self, name, status, id, manager)
        self.render = dp.newRender(self, 30, self.updateCallback, eventHandler=self.eventHandler)

    def updateCallback(self):
        dp.win.fill((255, 0, 0))
        entityManager.update()

    def eventHandler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                self.manager.switchWindow(self.id, 1)

    def update(self):
        self.render.update()

class Settings(win.Window):
    def __init__(self, name, status, id, manager):
        win.Window.__init__(self, name, status, id, manager)
        self.render = dp.newRender(self, 30, self.updateCallback, eventHandler=self.eventHandler)

    def eventHandler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.manager.switchWindow(self.id, 0)

    def updateCallback(self):
        dp.win.fill((0, 255, 0))

    def update(self):
        self.render.update()
