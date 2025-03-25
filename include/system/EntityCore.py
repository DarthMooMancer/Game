import pygame
from include.System.Display import win
from include.System.Settings import TILESIZE

class EntityManager:
    def __init__(self):
        self.groups: dict[str, pygame.sprite.Group] = {}

    def addGroup(self, name: str) -> None:
        self.groups[name] = pygame.sprite.Group()

    def addToGroup(self, nameOfObject, nameOfGroup) -> None:
        if nameOfGroup in self.groups:
            self.groups[nameOfGroup].add(nameOfObject)

    def update(self, name: str | None = None) -> None:
        if name is not None:
            if name in self.groups:
                self.groups[name].draw(win)
                self.groups[name].update()
        else:
            for group in self.groups.values():
                group.draw(win)
                group.update()

entityManager = EntityManager()
entityManager.addGroup("Entity")
entityManager.addGroup("Obstacles")

class Entity(pygame.sprite.Sprite):
    attributes: dict[str, int]
    def __init__(self, size, color, pos: tuple | int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.pos = pos
        self.rect = self.image.get_rect(center=(self.pos))
        self.attributes = {
            "speed": 6,
            "dx": 0,
            "dy": 0,
        }

    def update(self):
        pass

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(color)
        self.rect = pygame.Rect((x * TILESIZE, y * TILESIZE), (TILESIZE, TILESIZE))
