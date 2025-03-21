class Window:
    def __init__(self, id: int, manager):
        self.status: bool = False 
        self.id: int = id
        self.window: list[bool | int] = [self.status, id]
        self.manager = manager

    def getStatus(self) -> bool:
        return self.status

    def toggleState(self) -> None:
        if self.status:
            self.status = False
        else:
            self.status = True

    def setDisabled(self) -> None:
        self.status = False

    def getId(self) -> int:
        return self.id

    def getWindow(self) -> list[bool | int]:
        return self.window
    
    def update(self) -> None:
        pass

class windowManager(Window):
    def __init__(self):
        super().__init__(id=-1, manager=None)
        self.windows: list[Window] = []
        self.currentWindow: Window | None = None

    def __getDefaultWindow(self):
        for i in self.windows:
            if i.getId() == 0:
                self.currentWindow = i
                i.toggleState()

    def addWindow(self, window: Window):
        if not any(w.getId() == window.getId() for w in self.windows):
            self.windows.append(window)

    def removeWindow(self, window: Window):
        self.windows.remove(window)
 
    def baseUpdate(self):
        self.__getDefaultWindow()
        while True:
            if self.currentWindow is not None and self.currentWindow.getStatus() == True:
                self.currentWindow.update()
            else:
                print("currentWindow was either set to None or currentwindow is disabled")
                break

    def switchWindow(self, previousWindowId: int, nextWindowId: int):
        nextWindow = None
        for i in self.windows:
            if(i.getId() == previousWindowId):
                i.toggleState()
            if(i.getId() == nextWindowId):
                nextWindow = i
                nextWindow.toggleState()
        if nextWindow is not None and nextWindow.getStatus():
            self.currentWindow = nextWindow

        else:
            print("The next window is not properly status")

winManager = windowManager()
