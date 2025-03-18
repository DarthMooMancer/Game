import pygame
class Entity(pygame.sprite.Sprite):
    def __init__(self, size, color, pos: tuple):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.pos = pos
        self.rect = self.image.get_rect(center=(self.pos))

    def update(self):
        pass

class EntityManager:
    def __init__(self, window):
        self.groups = {}
        self.window = window

    def addGroup(self, name, group):
        self.groups[name] = group

    def removeGroup(self, name):
        self.groups.pop(name)

    def addToGroup(self, nameOfObject, nameOfGroup):
        if nameOfGroup in self.groups:
            self.groups[nameOfGroup].add(nameOfObject)

    def update(self):
        for group in self.groups.values():
            group.draw(self.window)
            group.update()
