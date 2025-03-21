import pygame
from include.system import EntityCore as ent
from include.system import Display as dp
from include.system.Settings import *

class Player(ent.Entity):
    mechanics: dict[str, bool]
    attributes: dict[str, int]
    def __init__(self):
        ent.Entity.__init__(self, 16, BLUE, (100, 100))
        self.mechanics = {
            "Up": False,
            "Down": False,
            "Left": False,
            "Right": False,
        }

        self.attributes = {
            "Speed": 4,
            "xVel": 0,
            "yVel": 0,
        }

    def clearVelocity(self):
        self.attributes["xVel"] = 0
        self.attributes["yVel"] = 0
        self.mechanics["Up"] = False
        self.mechanics["Down"] = False
        self.mechanics["Left"] = False
        self.mechanics["Right"] = False

    def eventHandler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.mechanics["Up"] = True
            if event.key == pygame.K_s:
                self.mechanics["Down"] = True
            if event.key == pygame.K_a:
                self.mechanics["Left"] = True
            if event.key == pygame.K_d:
                self.mechanics["Right"] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.mechanics["Up"] = False
                self.attributes["yVel"] = 0
            if event.key == pygame.K_s:
                self.mechanics["Down"] = False
                self.attributes["yVel"] = 0
            if event.key == pygame.K_a:
                self.mechanics["Left"] = False
                self.attributes["xVel"] = 0
            if event.key == pygame.K_d:
                self.mechanics["Right"] = False
                self.attributes["xVel"] = 0

    def movement(self):
        self.rect.x += self.attributes["xVel"]
        self.rect.y += self.attributes["yVel"]
        if self.mechanics["Up"]:
            self.attributes["yVel"] = -self.attributes["Speed"]
        if self.mechanics["Down"]:
            self.attributes["yVel"] = self.attributes["Speed"]
        if self.mechanics["Left"]:
            self.attributes["xVel"] = -self.attributes["Speed"]
        if self.mechanics["Right"]:
            self.attributes["xVel"] = self.attributes["Speed"]
        
    def update(self):
        self.movement()

class Wall(ent.Obstacle):
    def __init__(self, x, y, color):
        ent.Obstacle.__init__(self, x, y, color)
