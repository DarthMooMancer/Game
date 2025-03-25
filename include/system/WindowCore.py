from include.System.Display import newGraphicRender

class Window:
    def __init__(self, id: int, manager):
        self.status: bool = False 
        self.id: int = id
        self.manager = manager
        self.render = newGraphicRender(self, self.updateCallback, self.initCallback, self.eventHandler)

    def getStatus(self) -> bool:
        return self.status

    def getId(self) -> int:
        return self.id

    def toggleState(self) -> None:
        if self.status:
            self.status = False
        else:
            self.status = True

    def updateCallback(self) -> None:
        pass

    def initCallback(self) -> None:
        pass

    def eventHandler(self, event) -> None:
        pass

    def update(self) -> None:
        self.render.update()

class windowManager(Window):
    def __init__(self):
        super().__init__(id=-1, manager=None)
        self.windows: dict[int, Window] = {}
        self.currentWindow: Window | None = None

    def getDefaultWindow(self):
        if 0 in self.windows:
            self.currentWindow = self.windows[0]
            self.currentWindow.toggleState()

    def addWindow(self, id: int, window: Window):
        self.windows[id] = window

    def baseUpdate(self):
        self.getDefaultWindow()
        while True:
            if self.currentWindow is not None and self.currentWindow.getStatus():
                self.currentWindow.update()
            else:
                print("currentWindow was either set to None or currentwindow is disabled")
                break

    def switchWindow(self, previousWindowId: int, nextWindowId: int):
        if previousWindowId in self.windows and nextWindowId in self.windows:
            self.windows[previousWindowId].toggleState()
            nextWindow = self.windows[nextWindowId]
            self.windows[nextWindowId].toggleState()

            if nextWindow.getStatus():
                self.currentWindow = nextWindow

            else:
                print("The next window is not properly a window")
        else:
            print("One or both windows do not exist")

manager = windowManager()
