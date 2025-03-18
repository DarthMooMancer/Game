import pygame
from include import Entity as ent
from include import Display as dp
from include.Settings import *

# entityManager = ent.EntityManager(dp.win)

class Player(ent.Entity):
    def __init__(self):
        ent.Entity.__init__(self, 16, BLUE, (100, 100))
        
    def update(self):
        self.rect.x += 2

