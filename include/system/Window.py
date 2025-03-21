class Window:
    def __init__(self, id: int, manager):
        self.enabled: bool = False 
        self.id: int = id
        self.window: list[bool | int] = [self.enabled, id]
        self.manager = manager

    def getEnabled(self) -> bool:
        return self.enabled

    def setEnabled(self) -> None:
        self.enabled = True

    def setDisabled(self) -> None:
        self.enabled = False

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
                i.setEnabled()

    def addWindow(self, window: Window):
        if not any(w.getId() == window.getId() for w in self.windows):
            self.windows.append(window)

    def removeWindow(self, window: Window):
        self.windows.remove(window)
 
    def baseUpdate(self):
        self.__getDefaultWindow()
        while True:
            if self.currentWindow is not None and self.currentWindow.getEnabled() == True:
                self.currentWindow.update()
            else:
                print("currentWindow was either set to None or currentwindow is disabled")
                break

    def switchWindow(self, previousWindowId: int, nextWindowId: int):
        nextWindow = None
        for i in self.windows:
            if(i.getId() == previousWindowId):
                i.setDisabled()
            if(i.getId() == nextWindowId):
                nextWindow = i
                nextWindow.setEnabled()
        if nextWindow is not None and nextWindow.getEnabled():
            self.currentWindow = nextWindow

        else:
            print("The next window is not properly enabled")
