import pygame
from include.System.EntityCore import Entity, entityManager
from include.System.Settings import TILESIZE, WHITE, WIDTH, HEIGHT

class Player(Entity):
    def __init__(self):
        Entity.__init__(self, TILESIZE, WHITE, (100, 100))

    def movement(self):
        keys = pygame.key.get_pressed()
        self.attributes["dx"] = (keys[pygame.K_d] - keys[pygame.K_a]) * self.attributes["speed"]
        self.attributes["dy"] = (keys[pygame.K_s] - keys[pygame.K_w]) * self.attributes["speed"]
        self.rect.move_ip(self.attributes["dx"], self.attributes["dy"])

    def collision(self):
        self.collision_sprites = pygame.sprite.spritecollide(self, entityManager.groups["Obstacles"], False)
        self.padding = 5

        for sprite in self.collision_sprites:
            # Horizontal collision
            if self.attributes["dx"] > 0:  # Moving right
                self.rect.right = sprite.rect.left - self.padding
            elif self.attributes["dx"] < 0:  # Moving left
                self.rect.left = sprite.rect.right + self.padding

            # Vertical collision
            if self.attributes["dy"] > 0:  # Moving down
                self.rect.bottom = sprite.rect.top - self.padding
            elif self.attributes["dy"] < 0:  # Moving up
                self.rect.top = sprite.rect.bottom + self.padding

    def noOutOfBounds(self):
        self.padding = 5
        if self.rect.x < self.padding:
            self.rect.move_ip(-self.attributes["dx"], 0)
        if self.rect.x > WIDTH - TILESIZE - self.padding:
            self.rect.move_ip(-self.attributes["dx"], 0)
        if self.rect.y < self.padding:
            self.rect.move_ip(0, -self.attributes["dy"])
        if self.rect.y > HEIGHT - TILESIZE - self.padding:
            self.rect.move_ip(0, -self.attributes["dy"])

    def update(self):
        self.movement()
        self.noOutOfBounds()
        self.collision()
