from include import Window as win
from include import childWindows as cw

windowManager = win.windowManager()

main = cw.Main("Main", 0)
settings = cw.Settings("Settings", 1)

windowManager.addWindow(main)
windowManager.addWindow(settings)
windowManager.baseUpdate()

# myList = [ [1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9] ]
#
# myString = ""
# for row in myList:
#     for col in row:
#         myString += f"{col}, "
#     myString += "\n"
#
# print(myString)
