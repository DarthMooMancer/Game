import pygame
from include.System import EntityCore as ent
from include.System.Settings import *

class Player(ent.Entity):
    def __init__(self):
        ent.Entity.__init__(self, TILESIZE, WHITE, (100, 100))

    def movement(self):
        keys = pygame.key.get_pressed()
        self.attributes["dx"] = (keys[pygame.K_d] - keys[pygame.K_a]) * self.attributes["speed"]
        self.attributes["dy"] = (keys[pygame.K_s] - keys[pygame.K_w]) * self.attributes["speed"]
        self.rect.move_ip(self.attributes["dx"], self.attributes["dy"])

    def collision(self):
        if pygame.Rect.collidepoint(self.rect, 0, 0):
            self.rect.move_ip(-self.attributes["dx"], -self.attributes["dy"])

    def update(self):
        self.movement()
        self.collision()

class Wall(ent.Obstacle):
    def __init__(self, x, y, color):
        ent.Obstacle.__init__(self, x, y, color)
