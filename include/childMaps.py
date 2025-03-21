from include.system.Map import Map, mapManager

class Test(Map):
    def __init__(self):
        Map.__init__(self, matrix=[[1, 0], [0, 1]], id=1)

    def update(self):
        print("Test map updated")

test1 = Test()
mapManager.addMap(test1)
