from include.system import Window as win
from include import childWindows as cw

windowManager = win.windowManager()

main = cw.Main(0, windowManager)
settings = cw.Settings(1, windowManager)

windowManager.addWindow(main)
windowManager.addWindow(settings)
windowManager.baseUpdate()
