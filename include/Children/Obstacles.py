from include.System.EntityCore import Obstacle

class Wall(Obstacle):
    def __init__(self, x, y, color):
        Obstacle.__init__(self, x, y, color)

