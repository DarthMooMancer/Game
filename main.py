from include import childWindows as cw
from include.System import WindowCore as win

main = cw.Main(0, win.manager)
settings = cw.Settings(1, win.manager)

win.manager.addWindow(0, main)
win.manager.addWindow(1, settings)
win.manager.baseUpdate()
