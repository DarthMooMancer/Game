from include import Window as win
from include import ChildWindows as cw

windowManager = win.windowManager()

main = cw.Main("Main", False, 0, windowManager)
settings = cw.Settings("Settings", False, 1, windowManager)

windowManager.addWindow(main)
windowManager.addWindow(settings)
windowManager.baseUpdate()
