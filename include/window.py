class Window:
    def __init__(self, name, id):
        self.name: str = name
        self.enabled: bool = False 
        self.id: int = id
        self.window: list = [name, self.enabled, id]

    def getName(self):
        return self.name

    def getEnabled(self):
        return self.enabled

    def setEnabled(self):
        self.enabled = True

    def setDisabled(self):
        self.enabled = False

    def getId(self):
        return self.id

    def getWindow(self):
        return self.window
    
    def update(self):
        pass

class windowManager(Window):
    def __init__(self):
        super().__init__(name=None, id=None)
        self.windows = []
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
