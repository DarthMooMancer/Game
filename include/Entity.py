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

    def addGroup(self, name):
        self.groups[name] = pygame.sprite.Group()

    def removeGroup(self, name):
        self.groups.pop(name)

    def addToGroup(self, nameOfObject, nameOfGroup):
        if nameOfGroup in self.groups:
            self.groups[nameOfGroup].add(nameOfObject)

    def update(self, name=None):
        if name is not None:
            if name in self.groups:
                self.groups[name].draw(self.window)
                self.groups[name].update()
        else:
            for group in self.groups.values():
                group.draw(self.window)
                group.update()
