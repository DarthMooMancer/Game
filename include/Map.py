from include.Settings import *
from include import ChildEntities as chent

class Map:
    def __init__(self, matrix, id):
        self.matrix: list = matrix
        self.id: int = id

    def getMatrix(self) -> list:
        return self.matrix

    def getId(self) -> int:
        return self.id

    """ TODO
    Find a way to make it the map doesnt have tileRenderer and make it 
    everything can render based on number properly in MapManager. Below wont work
    because it is based on each map and can only use one group.

    """  

    def update(self):
        pass

class MapManager(Map):
    def __init__(self, group):
        Map.__init__(self, matrix=None, id=None)
        self.maps = []
        self.activeMap = []

    def addMap(self, map: Map):
        if not any(w.getId() == map.getId() for w in self.maps):
            self.maps.append(map)
        else:
            print("Map with that id already exists")

    def removeMap(self, map: Map):
        self.maps.remove(map)

    def tileRenderer(self):
        for row_index, row in enumerate(self.activeMap):
            for col_index, cell in enumerate(row):
                if cell == 1:
                    chent.Wall(row_index, col_index, BLUE)

                    pass

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
