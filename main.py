from include import window as win
from include import childWindows as cw

manager = win.windowManager()

main = cw.Main("Main", False, 0, manager)
settings = cw.Settings("Settings", False, 1, manager)

manager.addWindow(main)
manager.addWindow(settings)
manager.baseUpdate()
