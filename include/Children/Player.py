import pygame
from include.System.EntityCore import Entity 
from include.System.Settings import TILESIZE, WHITE

class Player(Entity):
    def __init__(self):
        Entity.__init__(self, TILESIZE, WHITE, (100, 100))

    def movementity(self):
        keys = pygame.key.get_pressed()
        self.attributes["dx"] = (keys[pygame.K_d] - keys[pygame.K_a]) * self.attributes["speed"]
        self.attributes["dy"] = (keys[pygame.K_s] - keys[pygame.K_w]) * self.attributes["speed"]
        self.rect.move_ip(self.attributes["dx"], self.attributes["dy"])

    def collision(self):
        if pygame.Rect.collidepoint(self.rect, 0, 0):
            self.rect.move_ip(-self.attributes["dx"], -self.attributes["dy"])

    def update(self):
        self.movementity()
        self.collision()
