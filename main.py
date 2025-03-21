from include.system import WindowCore as win
from include import childWindows as cw

main = cw.Main(0, win.winManager)
settings = cw.Settings(1, win.winManager)

win.winManager.addWindow(main)
win.winManager.addWindow(settings)
win.winManager.baseUpdate()
