import pygame
from include.system.Settings import * 
from include.system import Display as dp

class EntityManager:
    def __init__(self):
        self.groups: dict[str, pygame.sprite.Group] = {}

    def addGroup(self, name) -> None:
        self.groups[name] = pygame.sprite.Group()

    def removeGroup(self, name) -> None:
        self.groups.pop(name)

    def addToGroup(self, nameOfObject, nameOfGroup) -> None:
        if nameOfGroup in self.groups:
            self.groups[nameOfGroup].add(nameOfObject)

    def update(self, name=None) -> None:
        if name is not None:
            if name in self.groups:
                self.groups[name].draw(dp.win)
                self.groups[name].update()
        else:
            for group in self.groups.values():
                group.draw(dp.win)
                group.update()

entityManager = EntityManager()
entityManager.addGroup("Entity")
entityManager.addGroup("Obstacles")

class Entity(pygame.sprite.Sprite):
    def __init__(self, size, color, pos: tuple):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.pos = pos
        self.rect = self.image.get_rect(center=(self.pos))

    def update(self):
        pass

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(color)
        self.rect = pygame.Rect((x * TILESIZE, y * TILESIZE), (TILESIZE, TILESIZE))
