from include import Window as win
from include import ChildWindows as cw

windowManager = win.windowManager()

main = cw.Main("Main", 0, windowManager)
settings = cw.Settings("Settings", 1, windowManager)

windowManager.addWindow(main)
windowManager.addWindow(settings)
windowManager.baseUpdate()
