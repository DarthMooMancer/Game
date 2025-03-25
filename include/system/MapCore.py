from include.System.Settings import BLUE
from include.System.EntityCore import entityManager, Obstacle

class Map:
    def __init__(self, matrix: list[list[int]], id: int):
        self.matrix: list[list[int]] = matrix
        self.id: int = id

    def getMatrix(self) -> list[list[int]]:
        return self.matrix

    def getId(self) -> int:
        return self.id

    def update(self):
        pass

class MapManager:
    def __init__(self):
        self.maps = []
        self.activeMap = []

    def addMap(self, map: Map):
        if not any(w.getId() == map.getId() for w in self.maps):
            self.maps.append(map)
        else:
            print("Map with that id already exists")

    def tileRenderer(self):
        for row_index, row in enumerate(self.activeMap):
            for col_index, cell in enumerate(row):
                if cell == 1:
                    entityManager.addToGroup(Obstacle(row_index, col_index, BLUE), "Obstacles") # Creates a new Wall

    def setMap(self, map: Map):
        for i in self.maps:
            if i.getId() == map.getId():
                self.activeMap = map.getMatrix()

    def switchMaps(self, previousMap: int, nextMap: int):
        nextWindow = None
        for i in self.maps:
            if(i.getId() == previousMap):
                i.setDisabled()
            if(i.getId() == nextMap):
                nextWindow = i
                nextWindow.setEnabled()
        if nextWindow is not None and nextWindow.getEnabled():
            self.currentWindow = nextWindow

        else:
            print("The next window is not properly enabled")

mapManager = MapManager()
